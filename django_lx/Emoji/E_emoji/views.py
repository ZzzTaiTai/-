from django.shortcuts import render
from .models import IMG
from PIL import Image,ImageDraw,ImageFont
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')#直接使用render渲染返回即可Python

def uploadimg(request):
    if request.method == 'POST':
        new_img = IMG(
        img=request.FILES.get('img'),
        name = request.FILES.get('img').name)
        new_img.save()
    return render(request, 'uploadimg.html')
def showimg(request):
    imgs = IMG.objects.all()
    content={
        'imgs':imgs
    }
    return render(request, 'showimg.html', content)
