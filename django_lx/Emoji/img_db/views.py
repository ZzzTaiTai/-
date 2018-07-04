from django.shortcuts import render,HttpResponse
from .models import Img
from PIL import Image,ImageDraw,ImageFont

from io import BytesIO
import base64
# Create your views here.
'''
def uploadimg(request):
    if request.method == 'POST':
        new_img = Img(
        img=request.FILES.get('img'),
        name = request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'img_tem/uploadimg.html')
def showimg(request):
    imgs = Img.objects.all()
    content = {
    'imgs':imgs,
    }
    for i in imgs:
        print(i.img.url)
    return render(request, 'img_tem/showimg.html', content)'''
content = {}
imgs = Img.objects.all()
def index(request):
    if request.method == 'POST':
        new_img = Img(
            img=request.FILES.get('img'),
            name=request.FILES.get('img').name,
        )
        path = request.FILES.get('img').path
        img = Image.open(path)
        new_img.save()

        '''img =Image.open(new_images)
        n_img=ImageDraw.Draw(img)
        myFont = ImageFont.truetype(r'C:/windows/fonts/Arial.ttf', size=100)
        n_img.text((50, 50), '添加字体', fill="#ff0000", font=myFont)
        new_images.save()'''
        #handle_uploaded_file(success)
    content = {
        'imgs':imgs,
    }

    return render(request,'img_tem/index.html',content)





'''
 new_img=Img(
        img=request.FILES.get('img'),
        name=request.FILES.get('img').name
        )
        new_img.save()
    imgs =Img.objects.all()
    content = {
        'imgs':imgs,
    }
def makeit(request):
    if request.method == "POST":
    #imgs = Img.objects.all()
        base = Image.open(r'D:\django_lx\Emoji\media\img\0.gif')
        font = ImageFont.truetype(r'C:/windows/fonts/Arial.ttf', 40)
        d=ImageDraw.Draw(base)
        d.text((40,0),'添加字体',fill="#ff0000",font=font)
        buf =BytesIO()
        base.save(buf,format='png')
        image_stream =buf.getvalue()
        return HttpResponse(base64.b64encode(image_stream))
        image =Image.open(imgs[0])
        font = ImageFont.truetype(r'C:/windows/fonts/Arial.ttf', 40)
        d = ImageDraw.Draw(image)
        d.text((40, 0), '添加字体', fill="#ff0000", font=font)
        d.save() 
        
        
        for i in imgs:
        content2.append(i.img.url)
        im = Image.open(content2[len(content2)])
        n_img = ImageDraw.Draw(im)
        myFont = ImageFont.truetype(r'C:/windows/fonts/Arial.ttf', size=100)
        n_img.text((50, 50), '添加字体', fill="#ff0000", font=myFont)
        n_img.save()
        '''
