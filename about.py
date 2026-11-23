"""关于我：左边文字，右边立绘，色块和星星装饰。立绘以 base64 嵌进 SVG（<img> 引用的 SVG 不能加载外部图片）。"""
import base64
from PIL import Image
from deco import *

W, H = 760, 430
PANEL_Y = 0
img = Image.open("assets/lingmi.png")
FH = 418
FW = round(img.width * FH / img.height)
FX, FY = 430, H - FH - 6
b64 = base64.b64encode(open("assets/lingmi.png", "rb").read()).decode()

defs = f'''<clipPath id="apanel"><rect x="0" y="{PANEL_Y}" width="{W}" height="{H-PANEL_Y}" rx="24"/></clipPath>
<linearGradient id="abg" x1="0" y1="0" x2="1" y2="0.3">
  <stop offset="0" stop-color="#F7F4D2"/><stop offset="0.35" stop-color="#FCFBEC"/><stop offset="0.58" stop-color="#FFFFFF"/><stop offset="1" stop-color="#FFFFFF"/></linearGradient>
<radialGradient id="aglow" cx="0.5" cy="0.5" r="0.5">
  <stop offset="0" stop-color="#FFF1A8" stop-opacity="0.75"/><stop offset="0.6" stop-color="#FFF1A8" stop-opacity="0.25"/><stop offset="1" stop-color="#FFF1A8" stop-opacity="0"/></radialGradient>'''
style = f'''
      .ah {{ font: 700 26px {CJK}; fill: #4F5A2C; letter-spacing: 2px; }}
      .at {{ font: 400 16px {CJK}; fill: #6E6A3E; }}
      .hl {{ font: 500 16px {CJK}; fill: #6B8A3A; }}'''

body = f'''<rect x="0" y="{PANEL_Y}" width="{W}" height="{H-PANEL_Y}" rx="24" fill="#FFFFFF"/>
  <rect x="{FX+40}" y="70" width="{FW-60}" height="290" rx="28" fill="#FBF5D0"/>
  <rect x="{FX-6}" y="282" width="78" height="78" rx="18" fill="#E5EFC6"/>
  <rect x="{FX+FW-34}" y="52" width="46" height="46" rx="12" fill="#F3E79F" fill-opacity="0.7"/>
  {star(FX+FW-12, 120, 7, "#F2D64B", "tw")}{star(FX+22, 96, 5, "#C9DE94", "tw2")}{star(FX+FW+2, 300, 4.5, "#F2D64B", "tw2")}
  {star(330, 70, 5, "#F2D64B", "tw")}{star(362, 92, 3, "#C9DE94")}{star(260, 330, 4, "#F2D64B", "tw2")}
  <rect x="56" y="{PANEL_Y+330}" width="54" height="8" rx="4" fill="#F3E79F"/>
  <rect x="118" y="{PANEL_Y+330}" width="22" height="8" rx="4" fill="#D6E7AE"/>
  <image href="data:image/png;base64,{b64}" x="{FX}" y="{FY}" width="{FW}" height="{FH}"/>
  <g transform="translate(56 {PANEL_Y+110})">
    <g transform="translate(14 -9)" class="bob">{lemon(0, 0, 13)}</g>
    <text x="38" y="0" class="ah">关于我</text>
    <path d="M38 16 q 9 -5 18 0 t 18 0" fill="none" stroke="#A9CB78" stroke-width="2.4" stroke-linecap="round"/>
    <text x="0" y="62" class="at">我叫<tspan class="hl">晨露</tspan>，也可以叫我<tspan class="hl">柠弥</tspan></text>
    <text x="0" y="98" class="at">目前在为 AstrBot 写插件</text>
    <text x="0" y="134" class="at">欢迎来看我的主页～</text>
    <text x="0" y="170" class="at">有事可以发邮件给我：<tspan class="hl">chenluqwq@gmail.com</tspan></text>
  </g>'''
open("assets/about.svg", "w").write(svg(W, H, body, style, defs, "关于我：我叫晨露，也可以叫我柠弥"))
