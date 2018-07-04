from ..models import Post,Category,Tag
from django import template


register=template.Library()

#并将函数 get_recent_posts 装饰为 register.simple_tag
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

#这里 dates 方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间
# 且是 Python 的 date 对象，精确到月份，降序排列。
# created_time ，即 Post 的创建时间，month 是精度，order='DESC' 表明降序排列
@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()

