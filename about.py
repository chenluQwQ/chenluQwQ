"""关于我：左边文字，右边立绘，藤蔓小花装饰。立绘以 base64 嵌进 SVG（<img> 引用的 SVG 不能加载外部图片）。"""
import base64
from PIL import Image
from deco import *

W, H = 820, 430
PANEL_Y = 0
img = Image.open("assets/lingmi.png")
FH = 418
FW = round(img.width * FH / img.height)
FX, FY = W - FW - 30, H - FH - 6
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
  {vine(f"M-6 {H-40} C 40 {H-30}, 70 {H-70}, 120 {H-64} S 200 {H-36}, 250 {H-52} S 320 {H-80}, 350 {H-70}", 2)}
  {leaf(34, H-38, -30, .85)}{leaf(84, H-58, 200, .8, G2)}{leaf(150, H-62, -20, .75)}{leaf(214, H-44, 160, .7, G2)}{leaf(300, H-66, -40, .6, G3)}
  {flower(120, H-64, 7)}{flower(250, H-52, 5, "#FFF6C2", "#F2C230", 20)}{bud(350, H-70, 60)}
  {vine("M-6 40 C 30 46, 50 22, 90 24 S 150 44, 190 30 S 240 8, 262 14", 1.8, G3)}
  {leaf(28, 42, 30, .7, G2)}{leaf(70, 24, -150, .65)}{leaf(130, 36, 20, .6, G3)}{leaf(206, 24, -130, .55, G2)}
  {flower(90, 24, 6, "#FFFFFF", "#FFE066")}{flower(190, 30, 4.5, "#FFF6C2", "#F2C230")}{bud(262, 14, 70)}
  {flower(470, PANEL_Y+70, 3.2, "#FFFFFF", "#FFE680", 0, "tw")}{flower(536, PANEL_Y+250, 2.8, "#FFF6C2", "#FFD23F", 0, "tw2")}
  {dot(500, PANEL_Y+170, 1.8, "#FFE680")}{dot(790, PANEL_Y+230, 2)}{dot(440, PANEL_Y+300, 1.6)}
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
