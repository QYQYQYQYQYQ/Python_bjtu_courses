#authored by 邱烨卿-19271222
from PIL import Image
f1=Image.open("royal_never_give_up.jpeg")
f1.show()
#展示待处理图片
box = (140,0,380,500)
smller = f1.crop(box)
smller.show()
#处理并展示截取的埃菲尔铁塔的图片
f1.paste(smller,(483,0))
f1.show()
#z展示将截取的埃菲尔铁塔部分直接粘贴到原图中
f1.resize((50,100))
f1.show()
output=f1.rotate(90)
output.show()
#缩小尺寸并且将其逆时针旋转90度并展示
f1=Image.open("royal_never_give_up.jpeg")
r,g,b=f1.split()
f1=Image.merge('RGB',(b,g,r))
f1.show()
f1.close()
#图片在rgb模式下将每个像素点的b值与r值做变色处理
