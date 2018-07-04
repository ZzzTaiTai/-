from django.contrib import admin
from .models import Choice,Question
# Register your models here.
#Choice对象将在Question管理页面进行编辑，默认情况，请提供3个Choice对象的编辑区域。
#TabularInline表格内嵌,一种扁平化的显示方式
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    #属性
    fieldsets=[
        # 过滤器
        ('问题',{'fields':['question_text']}),
        ('最新时间',{'fields':['pub_date']}),
    ]
    #关联ChoiceInline
    inlines = [ChoiceInline]
    #搜索功能
    search_fields = ['question_text']
    #pub_date（过滤器）
    list_filter = ['pub_date']
    #list_display,按顺序显示每一个字段
    list_display = ('question_text','pub_date','was_published_recently')
admin.site.register(Question,QuestionAdmin)