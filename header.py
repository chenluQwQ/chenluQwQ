from deco import *

W, H = 1000, 272
SUB = "也可以叫我柠弥，欢迎来看我的主页"
FS = 20
n = len(SUB)
tw = n * FS
x0 = W / 2 - tw / 2
type_end, dur = 0.55, 10  # 前 55% 时间打字，之后停住，10 秒一轮
widths = [i * FS for i in range(n + 1)]
times = [round(type_end * i / n, 4) for i in range(n + 1)]
w_vals = ";".join(str(w) for w in widths + [tw])
k_vals = ";".join(str(t) for t in times + [1])
x_vals = ";".join(f"{x0 + w:.1f}" for w in widths + [tw])

defs = '''<linearGradient id="hbg" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#FFFEF4"/><stop offset="0.6" stop-color="#FAF6D2"/><stop offset="1" stop-color="#E9F2C8"/></linearGradient>
<linearGradient id="hbg2" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#DCEBB4" stop-opacity="0.7"/><stop offset="1" stop-color="#FFF3B0" stop-opacity="0.7"/></linearGradient>
<clipPath id="typing"><rect x="''' + f"{x0:.1f}" + '''" y="190" height="40" width="0">
  <animate attributeName="width" values="''' + w_vals + '''" keyTimes="''' + k_vals + f'''" dur="{dur}s" calcMode="discrete" repeatCount="indefinite"/>
</rect></clipPath>'''
style = f'''
      .pre {{ font: 400 20px {CJK}; fill: #7FA94E; letter-spacing: 2px; }}
      .hi {{ font: 600 56px {CJK}; fill: #4F5A2C; letter-spacing: 10px; }}
      .sub {{ font: 400 {FS}px {CJK}; fill: #7A7444; }}
      .cur {{ font: 400 {FS}px 'Menlo', 'Consolas', monospace; fill: #8DB255; }}'''

wave_back = "M0 0 H1000 V214 C 900 250, 800 196, 680 222 S 460 262, 330 228 S 110 206, 0 240 Z"
wave_front = "M0 0 H1000 V232 C 880 262, 760 214, 630 240 S 400 272, 270 240 S 90 222, 0 256 Z"

body = f'''<path d="{wave_back}" fill="url(#hbg2)"/>
  <path d="{wave_front}" fill="url(#hbg)"/>
  {vine("M-10 64 C 40 56, 60 22, 120 20 S 200 40, 250 8 S 300 -6, 330 -16")}
  {leaf(36, 56, -150, .9)}{leaf(72, 36, -60, 1, G2)}{leaf(150, 24, 20, .8)}{leaf(196, 32, -110, .75, G2)}{leaf(272, 2, 30, .65)}
  {flower(120, 20, 8)}{flower(226, 20, 5.5, "#FFF6C2", "#F2C230", 20)}{bud(300, 0, 30)}
  {vine("M1012 76 C 980 68, 962 40, 930 34 S 880 18, 860 -14", 2)}
  {leaf(984, 64, 160, .8, G2)}{leaf(948, 40, -40, .8)}{leaf(896, 26, 150, .7, G3)}{leaf(870, 4, -60, .6)}
  {flower(930, 34, 7)}{flower(990, 74, 4.5, "#FFF6C2", "#F2C230")}{bud(908, 16, -20)}
  {flower(330, 120, 3.4, "#FFFFFF", "#FFE680", 0, "tw")}{flower(690, 92, 3, "#FFF6C2", "#FFD23F", 0, "tw2")}
  {dot(250, 170, 2, "#FFE680")}{dot(760, 170, 2)}{dot(600, 40, 1.8)}
  <g class="bob">{lemon(900, 214, 26)}</g>
  <text x="500" y="84" text-anchor="middle" class="pre">Hi，我是</text>
  <text x="505" y="152" text-anchor="middle" class="hi">晨露</text>
  <path d="M470 170 q 10 -6 20 0 t 20 0 t 20 0" fill="none" stroke="#A9CB78" stroke-width="2.6" stroke-linecap="round"/>
  <text x="{x0:.1f}" y="216" class="sub" clip-path="url(#typing)">{SUB}</text>
  <rect x="{x0:.1f}" y="219" width="13" height="3" rx="1.5" fill="#8DB255"><animate attributeName="x" values="{x_vals}" keyTimes="{k_vals}" dur="{dur}s" calcMode="discrete" repeatCount="indefinite"/><animate attributeName="opacity" values="1;0" dur="1s" calcMode="discrete" repeatCount="indefinite"/></rect>'''
open("assets/header.svg", "w").write(svg(W, H, body, style, defs, "Hi，我是晨露"))
