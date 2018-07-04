from django.db import models
from PIL import Image,ImageDraw,ImageFont
from django import forms
# Create your models here.
class Img(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=50)
class text(models.Model):
    title=models.CharField(max_length=30)
    uploadfile=models.FileField(upload_to='files')
#class tetiploadForm(forms.Form):
