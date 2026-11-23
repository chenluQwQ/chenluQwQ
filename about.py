"""关于我：左边文字，右边立绘（白底原图，不抠图），金色星星点缀。立绘以 base64 嵌进 SVG（<img> 引用的 SVG 不能加载外部图片）。"""
import base64
from PIL import Image
from deco import *

W, H = 760, 430
img = Image.open("assets/lingmi.png")
FH = 400
FW = round(img.width * FH / img.height)
FX, FY = 440, 15
b64 = base64.b64encode(open("assets/lingmi.png", "rb").read()).decode()

body = f'''<rect width="{W}" height="{H}" fill="#FFFFFF"/>
  <image href="data:image/png;base64,{b64}" x="{FX}" y="{FY}" width="{FW}" height="{FH}"/>
  {star(FX-20, 290, 5, PALE, "tw")}{star(FX+FW+18, 150, 4, GOLD, "tw2")}
  <g transform="translate(56 110)">
    {title("关于我")}
    <text x="0" y="62" class="at">我叫<tspan class="hl">晨露</tspan>，也可以叫我<tspan class="hl">柠弥</tspan></text>
    <text x="0" y="98" class="at">目前在为 AstrBot 写插件</text>
    <text x="0" y="134" class="at">欢迎来看我的主页～</text>
    <text x="0" y="170" class="at">有事可以发邮件给我：<tspan class="hl">chenluqwq@gmail.com</tspan></text>
  </g>'''
open("assets/about-angel.svg", "w").write(svg(W, H, body, INK_STYLE, "", "关于我：我叫晨露，也可以叫我柠弥"))
