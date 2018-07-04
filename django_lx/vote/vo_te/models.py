import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)#模型字段
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    '''def test(self):
    #打印查看是否在最近一天发布的
        now = timezone.now()
        print(now)
        print(self.pub_date)
        now1 = now - datetime.timedelta(days=1)
        print(now1)
        '''
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True
    #简要说明
    was_published_recently.short_description='是否在最近的一天发布?'
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text