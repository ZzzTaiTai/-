from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic
from .models import Choice,Question
from django.utils import timezone
# Create your views here.

class IndexView(generic.ListView):
    template_name='vo_te/index.html'
    context_object_name='latest_question_list'

    def get_queryset(self):
        '''返回最新的五个已发布的问题'''
        return Question.objects.filter(
            #lte意味着返回所有pub_date小于或等于timezone.now(),lts是小于
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name='vo_te/detail.html'
    def get_queryset(self):
        '''返回最新的五个已发布的问题'''
        # lte意味着返回所有pub_date小于或等于timezone.now(),lts是小于
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name='vo_te/results.html'

def vote(request,question_id):
    p=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=p.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'vo_te/detail.html',{
            'question':p,
            'error_message':"You didn't select a choice."
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        #成功处理投票的数据后，自动跳转到结果页面，防止用户连续多次提交。
        return HttpResponseRedirect(reverse('vo_te:results',args=(p.id,)))

'''def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    #output=','.join([q.question_text for q in latest_question_list])
    context={'latest_question_list':latest_question_list}
    return render(request,'vo_te/index.html',context)

def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'vo_te/detail.html',{'question':question})

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'vo_te/results.html',{'question':question})
'''

