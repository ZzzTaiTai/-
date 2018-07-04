from PIL import Image,ImageDraw,ImageFont
def add_text(img):
    tu=ImageDraw.Draw(img)
    #fill_one="#ff0000"
    myFont = ImageFont.truetype(r'C:/windows/fonts/Arial.ttf', size=40)
    w,h=img.size
    tu.text((w-40,0),'添加字体',fill="#ff0000",font=myFont)
    img.save(r'C:\Users\lenovo\Desktop\py\添加成功的img\2.jpg')
    print("修改成功")
    print(img.size)

img=Image.open(r'C:\Users\lenovo\Desktop\py\添加成功的img\1.jpg')
add_text(img)