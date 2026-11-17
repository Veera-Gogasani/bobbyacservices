# -*- coding: utf-8 -*-
"""Original BOBBY artwork: service scenes drawn as SVG, exported as HD WebP.
Run: python3 art.py  -> static/assets/img/art/*.webp (+ .svg sources in art-src/)"""
import os, subprocess, math
from PIL import Image

NAVY = '#102C50'; NAVY2 = '#0B1F3A'; BLUE = '#1688D4'; CYAN = '#56C8FF'; ORANGE = '#FF9F43'; ORD = '#F2851F'
SKIN = '#B97A55'; SKIN_D = '#9C6342'; HAIR = '#241713'

DEFS = f'''<defs>
<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EEF6FC"/><stop offset="1" stop-color="#DCEBF7"/></linearGradient>
<linearGradient id="wallw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FBF5EC"/><stop offset="1" stop-color="#F1E6D6"/></linearGradient>
<linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E6D3BC"/><stop offset="1" stop-color="#D3BB9E"/></linearGradient>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7CCBF5"/><stop offset="1" stop-color="#CFEFFF"/></linearGradient>
<linearGradient id="dusk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFC98A"/><stop offset=".55" stop-color="#FFE2B8"/><stop offset="1" stop-color="#E9F4FB"/></linearGradient>
<linearGradient id="unit" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".7" stop-color="#F2F6FA"/><stop offset="1" stop-color="#DCE5EE"/></linearGradient>
<linearGradient id="steel" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#C9D3DD"/><stop offset=".35" stop-color="#F5F8FB"/><stop offset=".6" stop-color="#D6DEE6"/><stop offset="1" stop-color="#AEBBC8"/></linearGradient>
<linearGradient id="odu" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F7F9FB"/><stop offset="1" stop-color="#D5DDE5"/></linearGradient>
<linearGradient id="org" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFB667"/><stop offset="1" stop-color="{ORD}"/></linearGradient>
<linearGradient id="shirt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#173B69"/><stop offset="1" stop-color="{NAVY}"/></linearGradient>
<linearGradient id="copper" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#B8642F"/><stop offset=".5" stop-color="#E9A06A"/><stop offset="1" stop-color="#A45526"/></linearGradient>
<linearGradient id="air" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{CYAN}" stop-opacity=".95"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></linearGradient>
<radialGradient id="glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".9"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>
<radialGradient id="cglow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{CYAN}" stop-opacity=".45"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
<radialGradient id="oglow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{ORANGE}" stop-opacity=".35"/><stop offset="1" stop-color="{ORANGE}" stop-opacity="0"/></radialGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#0B1F3A" flood-opacity=".18"/></filter>
<filter id="sh2" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="6" stdDeviation="7" flood-color="#0B1F3A" flood-opacity=".22"/></filter>
<filter id="blur"><feGaussianBlur stdDeviation="18"/></filter>
<pattern id="brick" width="80" height="40" patternUnits="userSpaceOnUse"><rect width="80" height="40" fill="#E7C9AE"/><path d="M0 0H80M0 20H80M20 0V20M60 20V40" stroke="#D5AE8D" stroke-width="3"/></pattern>
<pattern id="mesh" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M0 0L10 10M10 0L0 10" stroke="#9FB6CB" stroke-width="1.4"/></pattern>
</defs>'''

def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{DEFS}{body}</svg>'

# ---------- components ----------
def room(w, h, floor_y, wall='wall'):
    return (f'<rect width="{w}" height="{h}" fill="url(#{wall})"/>'
            f'<rect y="{floor_y}" width="{w}" height="{h-floor_y}" fill="url(#floor)"/>'
            f'<rect y="{floor_y-14}" width="{w}" height="16" fill="#FFFFFF" opacity=".85"/>'
            f'<rect y="{floor_y}" width="{w}" height="6" fill="#C6AA88" opacity=".6"/>')

def window(x, y, w, h, sky='sky'):
    return (f'<g filter="url(#sh2)"><rect x="{x-14}" y="{y-14}" width="{w+28}" height="{h+28}" rx="10" fill="#FFFFFF"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="url(#{sky})"/>'
            f'<circle cx="{x+w*0.72}" cy="{y+h*0.3}" r="{min(w,h)*0.12}" fill="#FFE7A3" opacity=".95"/>'
            f'<path d="M{x} {y+h*0.78} q{w*0.2} -{h*0.12} {w*0.42} -{h*0.02} t{w*0.58} -{h*0.06} V{y+h} H{x}z" fill="#8FD39B" opacity=".7"/>'
            f'<rect x="{x+w/2-5}" y="{y}" width="10" height="{h}" fill="#FFFFFF"/><rect x="{x}" y="{y+h/2-5}" width="{w}" height="10" fill="#FFFFFF"/></g>')

def plant(x, y, s=1):
    leaves = ''.join(f'<ellipse cx="{x + dx*s}" cy="{y - dy*s}" rx="{14*s}" ry="{46*s}" fill="{c}" transform="rotate({r} {x + dx*s} {y - dy*s})"/>'
                     for dx, dy, r, c in [(-30, 70, -30, '#2E9E6A'), (30, 70, 30, '#2E9E6A'), (-12, 95, -10, '#3DB57B'), (14, 92, 12, '#3DB57B'), (0, 110, 0, '#4CC88B'), (-44, 46, -55, '#3DB57B'), (44, 46, 55, '#3DB57B')])
    return (f'<g>{leaves}<path d="M{x-48*s} {y-20*s} h{96*s} l-{10*s} {78*s} h-{76*s}z" fill="#FFFFFF" filter="url(#sh2)"/>'
            f'<rect x="{x-52*s}" y="{y-26*s}" width="{104*s}" height="{14*s}" rx="{7*s}" fill="#E9EEF3"/></g>')

def airflow(x, y, w, n=5, gap=34, amp=26):
    p = ''
    for i in range(n):
        yy = y + i * gap
        p += (f'<path d="M{x} {yy} C{x+w*0.25} {yy+amp} {x+w*0.45} {yy-amp} {x+w*0.7} {yy+amp*0.6} S{x+w} {yy} {x+w} {yy}" '
              f'fill="none" stroke="{CYAN}" stroke-width="{9-i}" stroke-linecap="round" opacity="{0.9-i*0.13}"/>')
    return p

def split_ac(x, y, s=1, open_panel=False, filt=False, coil=False):
    W, H = 560*s, 170*s
    g = f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{W}" height="{H}" rx="{44*s}" fill="url(#unit)" stroke="#D4E0EB" stroke-width="{2*s}"/>'
    g += f'<path d="M{x+30*s} {y+H-48*s} H{x+W-30*s}" stroke="#C9D7E4" stroke-width="{3*s}"/>'
    g += f'<rect x="{x+44*s}" y="{y+H-34*s}" width="{W-88*s}" height="{14*s}" rx="{7*s}" fill="{NAVY}" opacity=".85"/>'
    g += f'<rect x="{x+W-120*s}" y="{y+42*s}" width="{66*s}" height="{30*s}" rx="{8*s}" fill="{NAVY}"/><text x="{x+W-87*s}" y="{y+64*s}" font-family="Arial,Helvetica" font-weight="700" font-size="{19*s}" fill="{CYAN}" text-anchor="middle">24°</text>'
    g += f'<circle cx="{x+W-150*s}" cy="{y+57*s}" r="{5*s}" fill="#3EDC8B"/></g>'
    if open_panel:
        g += (f'<path d="M{x+18*s} {y+12*s} L{x+W-18*s} {y+12*s} L{x+W-40*s} {y-120*s} L{x+40*s} {y-120*s}z" fill="#FFFFFF" stroke="#D4E0EB" stroke-width="{2*s}" opacity=".97" filter="url(#sh2)"/>')
    if filt:
        g += (f'<g transform="rotate(-8 {x+W*0.3} {y+H})"><rect x="{x+60*s}" y="{y+H+30*s}" width="{230*s}" height="{120*s}" rx="{10*s}" fill="#FFFFFF" stroke="#9FB6CB" stroke-width="{4*s}"/>'
              f'<rect x="{x+72*s}" y="{y+H+42*s}" width="{206*s}" height="{96*s}" rx="{6*s}" fill="url(#mesh)"/></g>')
    if coil:
        fins = ''.join(f'<line x1="{x+40*s+i*12*s}" y1="{y+30*s}" x2="{x+40*s+i*12*s}" y2="{y+H-56*s}" stroke="#9FB6CB" stroke-width="{3*s}"/>' for i in range(int((W-80*s)/(12*s))))
        g += f'<rect x="{x+30*s}" y="{y+22*s}" width="{W-60*s}" height="{H-70*s}" rx="{14*s}" fill="#E3ECF5"/>{fins}'
    return g

def outdoor(x, y, s=1, pipes=True):
    W, H = 440*s, 330*s
    cx, cy, r = x + 165*s, y + 168*s, 118*s
    g = f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{W}" height="{H}" rx="{20*s}" fill="url(#odu)" stroke="#C3CED9" stroke-width="{2*s}"/>'
    g += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#E5ECF2" stroke="#AFBDCB" stroke-width="{5*s}"/>'
    g += ''.join(f'<circle cx="{cx}" cy="{cy}" r="{r*k}" fill="none" stroke="#C1CDD9" stroke-width="{2.5*s}"/>' for k in (0.82, 0.62, 0.42))
    g += f'<line x1="{cx-r}" y1="{cy}" x2="{cx+r}" y2="{cy}" stroke="#C1CDD9" stroke-width="{2.5*s}"/><line x1="{cx}" y1="{cy-r}" x2="{cx}" y2="{cy+r}" stroke="#C1CDD9" stroke-width="{2.5*s}"/>'
    for a in (0, 120, 240):
        g += f'<path d="M{cx} {cy} C{cx+30*s} {cy-30*s} {cx+90*s} {cy-40*s} {cx+96*s} {cy-6*s} C{cx+70*s} {cy+12*s} {cx+30*s} {cy+12*s} {cx} {cy}z" fill="{NAVY}" opacity=".78" transform="rotate({a} {cx} {cy})"/>'
    g += f'<circle cx="{cx}" cy="{cy}" r="{16*s}" fill="{ORANGE}"/>'
    g += ''.join(f'<rect x="{x+318*s}" y="{y+34*s+i*24*s}" width="{96*s}" height="{11*s}" rx="{5*s}" fill="#C9D4DE"/>' for i in range(11))
    g += f'<rect x="{x+26*s}" y="{y+H}" width="{50*s}" height="{18*s}" rx="{4*s}" fill="#9FB0C0"/><rect x="{x+W-76*s}" y="{y+H}" width="{50*s}" height="{18*s}" rx="{4*s}" fill="#9FB0C0"/></g>'
    if pipes:
        g += (f'<path d="M{x+W} {y+H-70*s} h{40*s} q{20*s} 0 {20*s} -{20*s} V{y-60*s}" fill="none" stroke="url(#copper)" stroke-width="{14*s}" stroke-linecap="round"/>'
              f'<path d="M{x+W} {y+H-36*s} h{70*s} q{20*s} 0 {20*s} -{20*s} V{y-60*s}" fill="none" stroke="#F4F6F8" stroke-width="{18*s}" stroke-linecap="round"/>'
              f'<rect x="{x+W-8*s}" y="{y+H-84*s}" width="{22*s}" height="{64*s}" rx="{5*s}" fill="#8B98A6"/>')
    return g

def technician(x, y, s=1, pose='up', flip=False, tool='screwdriver'):
    """Flat technician seen three-quarter from behind (no face), feet at (x+100*s, y+420*s)."""
    t = f'translate({x},{y}) scale({-s if flip else s},{s})' + (f' translate(-200,0)' if flip else '')
    arm_back = '<path d="M76 158 Q58 214 66 262" stroke="url(#shirt)" stroke-width="24" fill="none" stroke-linecap="round"/><path d="M66 250 L70 300" stroke="'+SKIN_D+'" stroke-width="18" stroke-linecap="round"/>'
    if pose == 'up':
        arm = f'<path d="M128 156 Q160 120 168 84" stroke="url(#shirt)" stroke-width="24" fill="none" stroke-linecap="round"/><path d="M168 86 L176 36" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/><circle cx="177" cy="30" r="12" fill="{SKIN}"/>'
        if tool == 'screwdriver':
            arm += f'<rect x="172" y="-14" width="12" height="34" rx="5" fill="{ORANGE}" transform="rotate(12 178 10)"/><rect x="176" y="-44" width="5" height="34" fill="#8C9AA8" transform="rotate(12 178 10)"/>'
        elif tool == 'spray':
            arm += f'<g transform="rotate(10 178 0)"><rect x="166" y="-36" width="26" height="54" rx="8" fill="{CYAN}"/><rect x="170" y="-52" width="16" height="18" rx="4" fill="#FFFFFF"/><path d="M186 -48 h18" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/></g>'
    elif pose == 'hold':
        arm = f'<path d="M128 158 Q148 214 146 262" stroke="url(#shirt)" stroke-width="24" fill="none" stroke-linecap="round"/><path d="M146 252 L148 300" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/>'
        arm += f'<g filter="url(#sh2)"><rect x="120" y="300" width="96" height="64" rx="10" fill="url(#org)"/><rect x="120" y="318" width="96" height="8" fill="#D9741A"/><path d="M146 300 v-14 h44 v14" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/></g>'
    elif pose == 'tablet':
        arm = f'<path d="M128 158 Q160 190 150 226" stroke="url(#shirt)" stroke-width="24" fill="none" stroke-linecap="round"/><path d="M150 222 L182 206" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/>'
        arm += f'<g transform="rotate(-18 196 196)"><rect x="176" y="160" width="62" height="84" rx="8" fill="{NAVY2}"/><rect x="182" y="168" width="50" height="62" rx="4" fill="{CYAN}" opacity=".85"/><path d="M190 200 l8 8 16-18" stroke="#FFFFFF" stroke-width="5" fill="none" stroke-linecap="round"/></g>'
    else:
        arm = ''
    body = f'''<g transform="{t}">
<ellipse cx="100" cy="422" rx="78" ry="12" fill="#0B1F3A" opacity=".18"/>
<path d="M70 250 h30 l-2 160 h-26z" fill="#1E3B60"/><path d="M104 250 h30 l6 158 h-28z" fill="#244672"/>
<path d="M60 412 h44 q4 -16 -12 -18 h-28z" fill="#1B1B1F"/><path d="M110 410 h46 q4 -16 -12 -18 h-30z" fill="#1B1B1F"/>
{arm_back}
<path d="M64 150 q0 -18 18 -22 h40 q18 4 18 22 l4 112 h-84z" fill="url(#shirt)"/>
<path d="M62 210 h82" stroke="{ORANGE}" stroke-width="8"/><circle cx="128" cy="176" r="9" fill="{ORANGE}"/><text x="128" y="180.5" font-family="Arial" font-weight="700" font-size="11" fill="#FFFFFF" text-anchor="middle">B</text>
<rect x="92" y="114" width="20" height="22" rx="6" fill="{SKIN_D}"/>
<circle cx="102" cy="94" r="30" fill="{SKIN}"/>
<path d="M72 96 q0 -34 32 -34 q26 0 28 26 q-14 -6 -30 -2 q-10 4 -12 26 q-14 -2 -18 -16z" fill="{HAIR}"/>
<ellipse cx="128" cy="98" rx="6" ry="9" fill="{SKIN_D}"/>
<path d="M70 82 q2 -28 34 -30 q30 0 32 26 z" fill="{NAVY}"/><path d="M118 74 q30 0 40 8 q-14 6 -40 4z" fill="{ORANGE}"/>
{arm}
</g>'''
    return body

def ladder(x, y, h, s=1):
    rungs = ''.join(f'<rect x="{x+6*s}" y="{y+40*s+i*70*s}" width="{88*s}" height="{10*s}" rx="{4*s}" fill="#E68A2E"/>' for i in range(int(h/(70*s))))
    return (f'<g><rect x="{x}" y="{y}" width="{14*s}" height="{h}" rx="{5*s}" fill="url(#org)" transform="rotate(-6 {x} {y+h})"/>'
            f'<rect x="{x+90*s}" y="{y}" width="{14*s}" height="{h}" rx="{5*s}" fill="url(#org)" transform="rotate(6 {x+90*s} {y+h})"/>{rungs}</g>')

def toolbox(x, y, s=1):
    return (f'<g filter="url(#sh2)"><rect x="{x}" y="{y}" width="{170*s}" height="{96*s}" rx="{12*s}" fill="url(#org)"/>'
            f'<rect x="{x}" y="{y+26*s}" width="{170*s}" height="{10*s}" fill="#D9741A"/><path d="M{x+50*s} {y} v-{24*s} h{70*s} v{24*s}" fill="none" stroke="{NAVY}" stroke-width="{11*s}" stroke-linejoin="round"/>'
            f'<rect x="{x+20*s}" y="{y-34*s}" width="{12*s}" height="{40*s}" rx="{4*s}" fill="#8C9AA8" transform="rotate(-18 {x+26*s} {y})"/>'
            f'<rect x="{x+136*s}" y="{y-30*s}" width="{10*s}" height="{36*s}" rx="{3*s}" fill="{BLUE}" transform="rotate(14 {x+140*s} {y})"/></g>')

def sparkle(x, y, r, c='#FFFFFF'):
    return f'<path d="M{x} {y-r} Q{x+r*0.18} {y-r*0.18} {x+r} {y} Q{x+r*0.18} {y+r*0.18} {x} {y+r} Q{x-r*0.18} {y+r*0.18} {x-r} {y} Q{x-r*0.18} {y-r*0.18} {x} {y-r}z" fill="{c}"/>'

def badge(x, y, r, icon='check', c=None):
    c = c or '#1FA855'
    ic = {'check': f'<path d="M{x-r*0.38} {y} l{r*0.26} {r*0.28} l{r*0.5} -{r*0.56}" stroke="#fff" stroke-width="{r*0.18}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
          'bolt': f'<path d="M{x+r*0.1} {y-r*0.55} l-{r*0.4} {r*0.65} h{r*0.32} l-{r*0.12} {r*0.5} l{r*0.42} -{r*0.66} h-{r*0.32}z" fill="#fff"/>'}[icon]
    return f'<g filter="url(#sh2)"><circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>{ic}</g>'

def gauge(x, y, r, c, ang):
    a = math.radians(ang)
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" stroke="{c}" stroke-width="{r*0.16}"/>'
            + ''.join(f'<line x1="{x+math.cos(math.radians(t))*r*0.72}" y1="{y+math.sin(math.radians(t))*r*0.72}" x2="{x+math.cos(math.radians(t))*r*0.84}" y2="{y+math.sin(math.radians(t))*r*0.84}" stroke="#7B8A99" stroke-width="2"/>' for t in range(150, 391, 30))
            + f'<line x1="{x}" y1="{y}" x2="{x+math.cos(a)*r*0.7}" y2="{y+math.sin(a)*r*0.7}" stroke="{NAVY}" stroke-width="{r*0.08}" stroke-linecap="round"/><circle cx="{x}" cy="{y}" r="{r*0.1}" fill="{NAVY}"/>')

def bubbles(pts):
    return ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" opacity=".85" stroke="{CYAN}" stroke-width="2"/>' for x, y, r in pts)

def glow(x, y, r, g='cglow'):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#{g})"/>'

# ---------- scenes ----------
SC = {}
SC['hero'] = (1200, 1290, room(1200, 1290, 1010) + window(70, 300, 330, 380) +
    glow(820, 330, 380) + split_ac(560, 230, 1.05) + airflow(600, 440, 520, 5, 40, 30) +
    ladder(560, 560, 450, 1.3) + technician(500, 420, 1.42, 'up') + plant(1080, 1060, 1.3) + toolbox(150, 990, 1.15) +
    sparkle(470, 240, 22, CYAN) + sparkle(1140, 470, 16, CYAN))
SC['ac_repair'] = (1600, 1000, f'<rect width="1600" height="1000" fill="url(#brick)"/><rect width="1600" height="1000" fill="#FFF6EC" opacity=".25"/>' +
    f'<rect y="800" width="1600" height="200" fill="#C7CFD8"/><rect y="800" width="1600" height="12" fill="#AAB5C1"/>' +
    glow(560, 520, 420, 'oglow') + f'<path d="M290 470 h560 M300 470 v350 M840 470 v350" stroke="#7B8794" stroke-width="12"/>' +
    outdoor(330, 460, 1.0) + technician(940, 250, 1.35, 'tablet') + toolbox(1290, 730, 1.0) +
    badge(860, 360, 52, 'bolt', ORD) + badge(960, 300, 40, 'check') + sparkle(250, 300, 22, '#FFFFFF'))
SC['ac_servicing'] = (1600, 1000, room(1600, 1000, 820) + window(80, 220, 300, 330) + glow(980, 300, 420) +
    split_ac(640, 170, 1.15, filt=True) + technician(470, 290, 1.25, 'up', tool='spray') +
    ''.join(sparkle(px_, py_, r, CYAN) for px_, py_, r in [(1300, 470, 22), (1230, 520, 13), (1370, 560, 15), (720, 150, 16)]) +
    plant(1460, 870, 1.15) + bubbles([(820, 470, 10), (850, 500, 7), (790, 505, 6)]))
SC['ac_install'] = (1600, 1000, f'<rect width="900" height="1000" fill="url(#wall)"/><rect x="900" width="700" height="1000" fill="url(#brick)"/>' +
    f'<rect x="870" width="60" height="1000" fill="#E9EEF3"/><rect y="830" width="900" height="170" fill="url(#floor)"/><rect x="930" y="830" width="670" height="170" fill="#C7CFD8"/>' +
    split_ac(240, 200, 1.05) + f'<path d="M800 260 H1040 V520" fill="none" stroke="url(#copper)" stroke-width="16" stroke-linecap="round" stroke-dasharray="1 0"/>' +
    f'<path d="M800 290 H1010 V520" fill="none" stroke="#F4F6F8" stroke-width="18" stroke-linecap="round"/>' +
    f'<path d="M1060 560 h430 M1080 560 v290 M1470 560 v290" stroke="#7B8794" stroke-width="10"/>' + outdoor(1060, 420, 0.95, pipes=False) +
    technician(330, 410, 1.0, 'up') + toolbox(80, 740, 0.95) +
    f'<g transform="rotate(-6 640 560)"><rect x="560" y="540" width="200" height="34" rx="8" fill="#F5C542"/><rect x="640" y="548" width="40" height="18" rx="9" fill="#BDEFC7"/><circle cx="660" cy="557" r="6" fill="#3DB57B"/></g>' +
    badge(820, 160, 44, 'check') + airflow(300, 400, 420, 4, 34, 24))
SC['ac_uninstall'] = (1600, 1000, room(1600, 1000, 800, 'wallw') + glow(800, 420, 460, 'oglow') +
    f'<g filter="url(#sh2)"><rect x="200" y="520" width="360" height="280" rx="10" fill="#D9A86C"/><path d="M200 600 h360" stroke="#C08B4F" stroke-width="8"/><rect x="340" y="520" width="80" height="80" fill="#E8C391"/></g>' +
    f'<g transform="rotate(-4 400 480)">{split_ac(170, 400, 0.72)}</g>' +
    f'<g><rect x="700" y="760" width="420" height="22" rx="10" fill="#5B6B7C"/><rect x="1080" y="420" width="20" height="360" rx="8" fill="#5B6B7C"/><circle cx="760" cy="800" r="30" fill="#2B2F36"/><circle cx="1060" cy="800" r="30" fill="#2B2F36"/></g>' +
    outdoor(680, 420, 0.86, pipes=False) + technician(1150, 250, 1.3, 'hold', flip=True) +
    f'<path d="M560 260 h260" stroke="{BLUE}" stroke-width="14" stroke-linecap="round" stroke-dasharray="2 26"/><path d="M820 236 l40 24 -40 24z" fill="{BLUE}"/>' +
    badge(1450, 230, 46, 'check'))
SC['ac_gas'] = (1600, 1000, f'<rect width="1600" height="1000" fill="url(#brick)"/><rect width="1600" height="1000" fill="#EAF6FF" opacity=".35"/><rect y="820" width="1600" height="180" fill="#C7CFD8"/>' +
    glow(520, 560, 420) + outdoor(200, 470, 1.0) +
    f'<g filter="url(#sh)"><rect x="830" y="420" width="300" height="120" rx="20" fill="#E9EEF3" stroke="#AFBDCB" stroke-width="4"/>{gauge(910, 480, 50, BLUE, -40)}{gauge(1050, 480, 50, "#E25B4B", -110)}</g>' +
    f'<path d="M870 540 C860 680 700 700 650 640" fill="none" stroke="{BLUE}" stroke-width="14" stroke-linecap="round"/>' +
    f'<path d="M1090 540 C1110 690 760 740 640 700" fill="none" stroke="#E25B4B" stroke-width="14" stroke-linecap="round"/>' +
    f'<path d="M980 540 C990 640 1230 650 1260 620" fill="none" stroke="#F5C542" stroke-width="14" stroke-linecap="round"/>' +
    f'<g filter="url(#sh)"><rect x="1210" y="470" width="150" height="350" rx="60" fill="{CYAN}"/><rect x="1250" y="430" width="70" height="56" rx="12" fill="#8C9AA8"/><rect x="1230" y="560" width="110" height="70" rx="10" fill="#FFFFFF" opacity=".85"/><path d="M1260 595 h50" stroke="{BLUE}" stroke-width="10" stroke-linecap="round"/></g>' +
    badge(1460, 300, 48, 'check') + sparkle(780, 330, 20, '#FFFFFF') + sparkle(1180, 360, 16, '#FFFFFF'))
SC['ac_deepclean'] = (1600, 1000, room(1600, 1000, 840) + glow(800, 330, 520) +
    split_ac(420, 230, 1.35, open_panel=True, coil=True) +
    f'<g transform="rotate(-20 1260 640)" filter="url(#sh)"><rect x="1200" y="560" width="70" height="140" rx="16" fill="{BLUE}"/><rect x="1215" y="520" width="40" height="50" rx="8" fill="#FFFFFF"/><path d="M1255 532 h60" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round"/></g>' +
    f'<path d="M1180 470 L1010 420 M1180 480 L1020 470 M1175 490 L1030 520" stroke="{CYAN}" stroke-width="8" stroke-linecap="round" opacity=".8"/>' +
    bubbles([(980, 420, 18), (940, 380, 12), (1000, 470, 14), (900, 440, 9), (620, 360, 14), (660, 400, 9), (580, 410, 11), (760, 380, 16), (820, 420, 8)]) +
    ''.join(sparkle(a, b, r, CYAN) for a, b, r in [(380, 200, 24), (1260, 230, 20), (300, 560, 14)]) + plant(200, 900, 1.1) + badge(1360, 300, 46, 'check'))
SC['fridge'] = (1600, 1200, room(1600, 1200, 980, 'wallw') +
    f'<rect x="0" y="560" width="620" height="420" fill="#FFFFFF"/><rect x="0" y="540" width="640" height="34" rx="6" fill="#D9C7AE"/><rect x="40" y="620" width="240" height="300" rx="10" fill="#F1E6D6"/><rect x="320" y="620" width="240" height="300" rx="10" fill="#F1E6D6"/>' +
    f'<rect x="60" y="200" width="520" height="220" rx="12" fill="#FFFFFF" filter="url(#sh2)"/>' + glow(1000, 520, 520) +
    f'<g filter="url(#sh)"><rect x="760" y="150" width="480" height="830" rx="30" fill="url(#steel)"/><line x1="1000" y1="150" x2="1000" y2="980" stroke="#9FAFBF" stroke-width="6"/>' +
    f'<rect x="968" y="330" width="14" height="240" rx="7" fill="#7B8A99"/><rect x="1018" y="330" width="14" height="240" rx="7" fill="#7B8A99"/>' +
    f'<rect x="1060" y="230" width="120" height="80" rx="12" fill="{NAVY}"/><text x="1120" y="282" font-family="Arial" font-weight="700" font-size="34" fill="{CYAN}" text-anchor="middle">4°C</text></g>' +
    technician(1230, 330, 1.55, 'tablet', flip=True) + badge(1290, 260, 50, 'check') +
    ''.join(sparkle(a, b, r, CYAN) for a, b, r in [(700, 220, 22), (1350, 470, 16)]) + plant(560, 520, 0.8))
SC['washer'] = (1600, 1200, room(1600, 1200, 1000) + window(1120, 200, 340, 380) + glow(700, 640, 520) +
    f'<g filter="url(#sh)"><rect x="440" y="360" width="520" height="640" rx="34" fill="url(#unit)" stroke="#D4E0EB" stroke-width="3"/><path d="M440 480 h520" stroke="#D4E0EB" stroke-width="4"/>' +
    f'<rect x="480" y="400" width="150" height="46" rx="12" fill="{NAVY}"/><circle cx="880" cy="424" r="26" fill="#EEF3F8" stroke="#AFBDCB" stroke-width="5"/><circle cx="800" cy="424" r="11" fill="{CYAN}"/>' +
    f'<circle cx="700" cy="720" r="200" fill="#E6EDF4" stroke="#AFBDCB" stroke-width="14"/><circle cx="700" cy="720" r="158" fill="{BLUE}" opacity=".9"/>' +
    f'<path d="M550 760 q50 -46 100 0 t100 0 t100 0 v80 q-150 110 -300 0z" fill="{CYAN}" opacity=".95"/><circle cx="640" cy="660" r="24" fill="#FFFFFF" opacity=".55"/><circle cx="740" cy="640" r="14" fill="#FFFFFF" opacity=".5"/></g>' +
    f'<g filter="url(#sh2)"><path d="M1040 860 h260 l-24 140 h-212z" fill="#E8D3B5"/><ellipse cx="1170" cy="860" rx="140" ry="22" fill="#D8BD97"/><path d="M1080 850 q40 -50 90 -10 q40 -40 90 10" fill="{CYAN}"/><path d="M1110 852 q50 -30 110 0" fill="{ORANGE}"/></g>' +
    technician(90, 360, 1.55, 'hold') + badge(980, 330, 50, 'check') + bubbles([(560, 560, 12), (600, 530, 8), (840, 590, 10)]))
SC['cooler'] = (1600, 1200, room(1600, 1200, 1000, 'wallw') + window(140, 220, 360, 420, 'dusk') + glow(860, 560, 520) +
    f'<g filter="url(#sh)"><rect x="660" y="300" width="400" height="700" rx="46" fill="url(#unit)" stroke="#D4E0EB" stroke-width="3"/>' +
    f'<rect x="710" y="360" width="300" height="300" rx="24" fill="#E6EDF4" stroke="#AFBDCB" stroke-width="5"/>' +
    ''.join(f'<rect x="730" y="{385+i*36}" width="260" height="14" rx="7" fill="#AFBDCB"/>' for i in range(7)) +
    f'<rect x="710" y="700" width="300" height="160" rx="18" fill="{BLUE}" opacity=".14"/><rect x="710" y="780" width="300" height="80" rx="14" fill="{CYAN}" opacity=".7"/>' +
    f'<circle cx="760" cy="920" r="20" fill="{NAVY}"/><circle cx="860" cy="920" r="20" fill="{ORANGE}"/><circle cx="960" cy="920" r="20" fill="{NAVY}"/></g>' +
    airflow(1080, 420, 420, 5, 46, 34) + plant(1420, 1050, 1.2) + badge(1080, 300, 50, 'check') +
    ''.join(sparkle(a, b, r, CYAN) for a, b, r in [(1180, 360, 18), (1460, 700, 14)]))
SC['fan'] = (1600, 1200, f'<rect width="1600" height="1200" fill="url(#wallw)"/><rect width="1600" height="160" fill="#FFFFFF"/><rect y="150" width="1600" height="14" fill="#E9DFD0"/>' +
    f'<rect y="1010" width="1600" height="190" fill="url(#floor)"/>' + glow(800, 470, 560) +
    f'<rect x="788" y="150" width="24" height="200" fill="#8C9AA8"/><rect x="750" y="150" width="100" height="34" rx="10" fill="#C9D3DD"/>' +
    f'<g transform="translate(800,420)"><ellipse rx="560" ry="70" fill="{CYAN}" opacity=".12"/><ellipse rx="420" ry="52" fill="none" stroke="{CYAN}" stroke-width="6" opacity=".35" stroke-dasharray="40 60"/>' +
    f'<g filter="url(#sh)"><path d="M0 0 C-80 -40 -330 -36 -420 -6 C-330 26 -80 30 0 0z" fill="{NAVY}" opacity=".92"/><path d="M0 0 C80 -40 330 -36 420 -6 C330 26 80 30 0 0z" fill="{NAVY}" opacity=".92"/>' +
    f'<path d="M0 0 C-40 30 -70 120 -60 160 C-20 130 10 40 0 0z" fill="{NAVY}" opacity=".8"/><ellipse rx="70" ry="44" fill="url(#steel)"/><ellipse cy="26" rx="54" ry="24" fill="#FFF3D6"/><circle r="14" fill="{ORANGE}"/></g></g>' +
    window(1140, 420, 300, 380) + f'<rect x="120" y="760" width="460" height="250" rx="30" fill="{BLUE}" opacity=".85" filter="url(#sh)"/><rect x="140" y="700" width="420" height="110" rx="26" fill="#2E7FC0"/>' +
    badge(1300, 270, 50, 'check') + ''.join(sparkle(a, b, r, CYAN) for a, b, r in [(320, 330, 20), (1250, 620, 14)]))
SC['about'] = (1600, 1280, f'<rect width="1600" height="1280" fill="url(#dusk)"/>' + glow(1180, 300, 300) +
    f'<circle cx="1180" cy="300" r="90" fill="#FFE29A"/>' +
    ''.join(f'<g filter="url(#sh2)"><rect x="{x}" y="{y}" width="{w}" height="{1000-y}" fill="{c}"/>' + ''.join(f'<rect x="{x+24+j*((w-48)//2)}" y="{y+40+k*120}" width="{(w-72)//2}" height="70" rx="6" fill="#FFFFFF" opacity=".75"/>' for j in range(2) for k in range(max(1, (1000-y-80)//120))) + '</g>'
            for x, y, w, c in [(40, 520, 300, '#F4D9B5'), (340, 440, 280, '#CFE3F2'), (1000, 480, 300, '#F6C9A0'), (1300, 560, 280, '#D9EBDD')]) +
    f'<g><rect x="1290" y="430" width="20" height="560" fill="#7A5A3A"/>' + ''.join(f'<ellipse cx="1300" cy="430" rx="130" ry="26" fill="#2E9E6A" transform="rotate({r} 1300 430)"/>' for r in (0, 35, 70, 110, 145, 180, -35)) + '</g>' +
    f'<rect y="1000" width="1600" height="280" fill="#C7CFD8"/><rect y="1000" width="1600" height="14" fill="#AAB5C1"/>' +
    technician(560, 340, 1.6, 'hold') +
    outdoor(170, 720, 0.6, pipes=False) + split_ac(380, 300, 0.45) + badge(900, 380, 54, 'check'))


def embed(path, x, y, w=None, h=None):
    """Embed one of the BOBBY appliance renders (PNG data URI) into a scene."""
    import base64, io
    im = Image.open(path).convert('RGBA')
    if h and not w: w = h * im.width / im.height
    if w and not h: h = w * im.height / im.width
    buf = io.BytesIO(); im.save(buf, 'PNG')
    return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="data:image/png;base64,{base64.b64encode(buf.getvalue()).decode()}"/>'

# 'Why choose BOBBY' scene – flat illustration in the website navy theme
def flat_fridge(x, y, s=1):
    W, H = 300*s, 560*s
    return (f'<g><rect x="{x+10*s}" y="{y+H-6*s}" width="{W-20*s}" height="{14*s}" rx="{7*s}" fill="#081629" opacity=".5"/>'
            f'<rect x="{x}" y="{y}" width="{W}" height="{H}" rx="{22*s}" fill="#EEF3F8"/>'
            f'<rect x="{x+W/2}" y="{y}" width="{W/2}" height="{H}" rx="{22*s}" fill="#DFE8F1"/><rect x="{x+W/2}" y="{y}" width="{24*s}" height="{H}" fill="#DFE8F1"/>'
            f'<rect x="{x+W/2-2*s}" y="{y}" width="{4*s}" height="{H}" fill="#C3D1DE"/>'
            f'<rect x="{x+W/2-26*s}" y="{y+110*s}" width="{12*s}" height="{170*s}" rx="{6*s}" fill="#AFC0D0"/><rect x="{x+W/2+14*s}" y="{y+110*s}" width="{12*s}" height="{170*s}" rx="{6*s}" fill="#AFC0D0"/>'
            f'<rect x="{x+30*s}" y="{y+110*s}" width="{70*s}" height="{100*s}" rx="{10*s}" fill="{NAVY}"/>'
            f'<text x="{x+65*s}" y="{y+152*s}" font-family="Arial,Helvetica" font-weight="700" font-size="{20*s}" fill="{CYAN}" text-anchor="middle">3°</text>'
            f'<rect x="{x+48*s}" y="{y+166*s}" width="{34*s}" height="{30*s}" rx="{5*s}" fill="#081629"/>'
            f'<rect x="{x+18*s}" y="{y+H}" width="{30*s}" height="{10*s}" rx="{3*s}" fill="#56677A"/><rect x="{x+W-48*s}" y="{y+H}" width="{30*s}" height="{10*s}" rx="{3*s}" fill="#56677A"/></g>')

def flat_washer(x, y, s=1):
    W, H = 300*s, 340*s
    cx, cy = x + W/2, y + 200*s
    return (f'<g><rect x="{x}" y="{y}" width="{W}" height="{H}" rx="{24*s}" fill="#EEF3F8"/>'
            f'<rect x="{x}" y="{y}" width="{W}" height="{70*s}" rx="{24*s}" fill="#FFFFFF"/><rect x="{x}" y="{y+46*s}" width="{W}" height="{24*s}" fill="#FFFFFF"/>'
            f'<rect x="{x+24*s}" y="{y+20*s}" width="{80*s}" height="{30*s}" rx="{7*s}" fill="{NAVY}"/>'
            f'<text x="{x+64*s}" y="{y+41*s}" font-family="Arial,Helvetica" font-weight="700" font-size="{16*s}" fill="{CYAN}" text-anchor="middle">0:42</text>'
            + ''.join(f'<circle cx="{x+130*s+i*24*s}" cy="{y+35*s}" r="{6*s}" fill="{ORANGE if i == 3 else "#C3D1DE"}"/>' for i in range(4)) +
            f'<circle cx="{x+W-36*s}" cy="{y+35*s}" r="{17*s}" fill="#DFE8F1"/><rect x="{x+W-38*s}" y="{y+22*s}" width="{4*s}" height="{12*s}" rx="{2*s}" fill="{NAVY}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{108*s}" fill="#C9D6E3"/><circle cx="{cx}" cy="{cy}" r="{88*s}" fill="{BLUE}"/>'
            f'<path d="M{cx-88*s} {cy+10*s} q{44*s} -{26*s} {88*s} 0 t{88*s} 0 A{88*s} {88*s} 0 0 1 {cx-88*s} {cy+10*s}z" fill="{CYAN}"/>'
            f'<path d="M{cx-52*s} {cy-48*s} a{70*s} {70*s} 0 0 1 {50*s} -{20*s}" stroke="#FFFFFF" stroke-width="{10*s}" fill="none" stroke-linecap="round" opacity=".8"/>'
            f'<circle cx="{cx+40*s}" cy="{cy+40*s}" r="{7*s}" fill="#FFFFFF" opacity=".85"/><circle cx="{cx+18*s}" cy="{cy+56*s}" r="{4*s}" fill="#FFFFFF" opacity=".85"/></g>')

_WHY_BG = (f'<defs><linearGradient id="nvbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#16477A"/><stop offset=".6" stop-color="{NAVY}"/><stop offset="1" stop-color="{NAVY2}"/></linearGradient>'
           f'<pattern id="dots" width="34" height="34" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.6" fill="#FFFFFF" opacity=".09"/></pattern></defs>'
           f'<rect width="1200" height="1440" fill="url(#nvbg)"/><rect width="1200" height="1260" fill="url(#dots)"/>')
SC['why'] = (1200, 1440, _WHY_BG + f'<circle cx="600" cy="360" r="460" fill="{CYAN}" opacity=".08"/><circle cx="600" cy="360" r="300" fill="{CYAN}" opacity=".07"/>' +
    split_ac(236, 190, 1.3) + airflow(270, 450, 680, 5, 48, 34) +
    sparkle(1070, 170, 26, CYAN) + sparkle(170, 380, 18, CYAN) + sparkle(1120, 620, 14, '#FFFFFF') +
    f'<rect y="1260" width="1200" height="180" fill="#0A1B33"/><rect y="1256" width="1200" height="6" fill="{CYAN}" opacity=".3"/>' +
    f'<ellipse cx="600" cy="1300" rx="520" ry="26" fill="#000" opacity=".18"/>' +
    flat_washer(40, 920, 1.05) +
    ladder(470, 630, 640, 1.4) + technician(400, 440, 1.75, 'up') + toolbox(650, 1180, 0.85) +
    flat_fridge(850, 690, 1.0) +
    badge(1080, 330, 46, 'check', '#1FA855') + badge(110, 800, 34, 'bolt', ORANGE))

def build(outdir='static/assets/img/art', srcdir='art-src', only=None):
    os.makedirs(outdir, exist_ok=True); os.makedirs(srcdir, exist_ok=True)
    for name, (w, h, body) in SC.items():
        if only and name not in only: continue
        sp = os.path.join(srcdir, name + '.svg'); open(sp, 'w').write(svg(w, h, body))
        png = f'/tmp/{name}.png'
        subprocess.run(['rsvg-convert', '-w', str(w), sp, '-o', png], check=True)
        im = Image.open(png).convert('RGB')
        im.save(os.path.join(outdir, name + '-lg.webp'), quality=88, method=6)
        im.resize((w // 2, h // 2), Image.LANCZOS).save(os.path.join(outdir, name + '-sm.webp'), quality=86, method=6)
    print('art built:', ', '.join(SC))

if __name__ == '__main__':
    import sys
    build(only=sys.argv[1:] or None)
