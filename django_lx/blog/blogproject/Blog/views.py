import markdown
from django.shortcuts import render,get_object_or_404
from comments.forms import CommentForm
from django.contrib.auth.models import User
from .models import Post,Category
from  django.views.generic import ListView,DetailView
# Create your views here.
from django.http import HttpResponse

class IndexView(ListView):
    model = Post
    template_name = 'Blog/index.html'
    context_object_name = 'post_list'
    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 2

    def get_context_data(self, **kwargs):

        context=super().get_context_data(**kwargs)
        paginator=context.get('paginator')
        page=context.get('page_obj')
        is_paginated=context.get('is_paginated')

        pagination_data=self.pagination_data(paginator,page,is_paginated)

        context.update(pagination_data)

        return context

    def pagination_data(self,paginator,page,is_paginated):

        #没有分页，返回空
        if not is_paginated:
            return {}

        # 当前页左边连续的页码号，初始值为空
        left = []

        # 当前页右边连续的页码号，初始值为空
        right = []

        # 标示第 1 页页码后是否需要显示省略号
        left_has_more = False

        # 标示最后一页页码前是否需要显示省略号
        right_has_more = False

        # 标示是否需要显示第 1 页的页码号。
        # 因为如果当前页左边的连续页码号中已经含有第 1 页的页码号，此时就无需再显示第 1 页的页码号，
        # 其它情况下第一页的页码是始终需要显示的。
        # 初始值为 False
        first = False

        # 标示是否需要显示最后一页的页码号。
        # 需要此指示变量的理由和上面相同。
        last = False

        #当前请求的页码
        page_number = page.number

        #分页后的总页数
        total_pages = paginator.num_pages

        #分页页码列表，比如分了四页，那么就是 [1, 2, 3, 4]
        page_range = paginator.page_range

        if page_number == 1:
            right = page_range[page_number:page_number+2]

            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[(page_number-3) if (page_number-3)>0 else 0:page_number-1]


            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            right = page_range[page_number:page_number + 2]
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True

            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        data = {
            'left':left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }
        return data


class CategoryView(IndexView):
    def get_queryset(self):
        cate=get_object_or_404(Category,pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category=cate)

class ArchivesView(IndexView):
    def get_queryset(self):
        month=self.kwargs.get('month')
        year=self.kwargs.get('year')
        return super().get_queryset().filter(created_time__year=year,
                                  created_time__month=month)



'''
def index(request):
    post_list = Post.objects.all()
    return render(request,'Blog/index.html',context={
        'post_list':post_list
    })
    '''
class PostDetailView(DetailView):
    model = Post
    template_name = 'Blog/detail.html'
    context_object_name = 'post'

    def get(self,request,*args,**kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response =super().get(request,*args,**kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super().get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])

        return post

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data 的目的是因为除了
        # 将 post 传递给模板外（DetailView 已经帮我们完成）
        # 还要把评论表单、post 下的评论列表传递给模板。
        context=super().get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
                   'form': form,
                   'comment_list': comment_list
                   })
        return context


'''
def detail(request,pk):
   post = get_object_or_404(Post,pk=pk)
   post.increase_views()
   post.body = markdown.markdown(post.body,
                                 extensions=[
                                   'markdown.extensions.extra',
                                   'markdown.extensions.codehilite',
                                   'markdown.extensions.toc',
                               ])

   form = CommentForm()
   comment_list = post.comment_set.all()
   context = {'post': post,
              'form': form,
              'comment_list': comment_list
              }
   return render(request,'Blog/detail.html',context=context)
'''
#因此这里根据文章发表的年和月来过滤。具体来说
# 就是根据 created_time 的 year 和 month 属性过滤
# 筛选出文章发表在对应的 year 年和 month 月的文章。
# 注意这里 created_time 是 Python 的 date 对象，其有一个 year 和 month 属性
def archives(request,year,month):
    post_list=Post.objects.filter(created_time__year=year,
                                  created_time__month=month).order_by('-created_time')
    return render(request,'Blog/index.html',context={'post_list':post_list})

def category(request,pk):
    cate=get_object_or_404(Category,pk=pk)
    post_list=Post.objects.filter(category=cate).order_by('-created_time')
    return render(request,'Blog/index.html',context={'post_list':post_list})

def author(request,pk):
    user=get_object_or_404(User,pk=pk)
    post_list=Post.objects.filter(author=user).order_by('-created_time')
    return render(request,'Blog/index.html',context={'post_list': post_list})