from PIL import Image, ImageDraw, ImageFont
import random, string, io
from django.shortcuts import HttpResponse, render

# 返回随机色
def rndColor():
    c1 = random.randrange(0,255)
    c2 = random.randrange(0,255)
    c3 = random.randrange(0,255)
    return (c1,c2,c3)


def verifycode(request):
    '''生成随机验证码，返回验证码图片并将随机字符保存进session'''
    # 得到随机码
    base_str = string.ascii_letters + string.digits
    rnd_list = random.sample(base_str,4)
    rnd_str = ''.join(rnd_list)

    # 创建图片对象
    bgcolor = 'gray'
    width,height = 80,25
    img = Image.new('RGB',(width,height),bgcolor)

    # 创建画笔对象并书写验证码
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf',20)
    font_color = rndColor()
    draw.text((15,2),rnd_str,font_color,font)

    # 开辟二进制内存空间，存储图片
    buf = io.BytesIO()
    img.save(buf,'png')
    request.session['verifycode'] = rnd_str.lower()
    
    return HttpResponse(buf.getvalue())
