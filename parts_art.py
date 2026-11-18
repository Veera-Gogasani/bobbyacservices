# -*- coding: utf-8 -*-
"""Original product-style illustrations for the AC spare parts page (drawn here – no third-party photos).
Run: python3 parts_art.py [key ...]  ->  static/assets/img/parts/<key>.webp  (480x480, shown at ~160px)"""
import os, sys, math, subprocess
from PIL import Image

W = 480
DEFS = '''<defs>
<radialGradient id="bg" cx=".5" cy=".42" r=".75"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#E6F1FA"/></radialGradient>
<radialGradient id="sh" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#0B1F3A" stop-opacity=".28"/><stop offset="1" stop-color="#0B1F3A" stop-opacity="0"/></radialGradient>
<linearGradient id="brass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F7DC8A"/><stop offset=".45" stop-color="#D4A93F"/><stop offset="1" stop-color="#9A7322"/></linearGradient>
<linearGradient id="brassv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F7DC8A"/><stop offset=".5" stop-color="#D2A63C"/><stop offset="1" stop-color="#9A7322"/></linearGradient>
<linearGradient id="cu" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F4B08A"/><stop offset=".45" stop-color="#C8693A"/><stop offset="1" stop-color="#8A3E1C"/></linearGradient>
<linearGradient id="cuh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8A3E1C"/><stop offset=".5" stop-color="#E9996E"/><stop offset="1" stop-color="#8A3E1C"/></linearGradient>
<linearGradient id="steel" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8E9AA8"/><stop offset=".35" stop-color="#E9EEF3"/><stop offset=".7" stop-color="#B6C0CB"/><stop offset="1" stop-color="#7C8896"/></linearGradient>
<linearGradient id="steelv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EEF2F6"/><stop offset=".6" stop-color="#B9C3CE"/><stop offset="1" stop-color="#8592A1"/></linearGradient>
<linearGradient id="dark" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1B2633"/><stop offset=".4" stop-color="#4A5868"/><stop offset="1" stop-color="#16202B"/></linearGradient>
<linearGradient id="darkv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4A5868"/><stop offset="1" stop-color="#16202B"/></linearGradient>
<linearGradient id="white" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#D9E2EC"/></linearGradient>
<linearGradient id="whiteh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#CFD9E4"/><stop offset=".4" stop-color="#FFFFFF"/><stop offset="1" stop-color="#C3CEDA"/></linearGradient>
<linearGradient id="pcb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2F8F5B"/><stop offset="1" stop-color="#145233"/></linearGradient>
<linearGradient id="pcbb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2A6FB8"/><stop offset="1" stop-color="#123D6E"/></linearGradient>
<linearGradient id="blue" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#56C8FF"/><stop offset="1" stop-color="#1572B8"/></linearGradient>
<linearGradient id="orange" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFC27A"/><stop offset="1" stop-color="#E9761A"/></linearGradient>
<linearGradient id="foam" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1E2A36"/><stop offset=".5" stop-color="#3B4856"/><stop offset="1" stop-color="#1E2A36"/></linearGradient>
<linearGradient id="fin" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#AEB9C5"/><stop offset=".5" stop-color="#E8EDF2"/><stop offset="1" stop-color="#AEB9C5"/></linearGradient>
<pattern id="fins" width="10" height="10" patternUnits="userSpaceOnUse"><rect width="10" height="10" fill="#D7DFE7"/><rect width="3" height="10" fill="#A9B5C2"/></pattern>
<pattern id="mesh" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#F4F7FA"/><path d="M0 0L8 8M8 0L0 8" stroke="#B9C6D3" stroke-width="1"/></pattern>
</defs>'''


def frame(body, shadow=(240, 400, 150, 22)):
    sx, sy, rx, ry = shadow
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{W}" viewBox="0 0 {W} {W}">{DEFS}'
            f'<rect width="{W}" height="{W}" fill="url(#bg)"/>'
            f'<ellipse cx="{sx}" cy="{sy}" rx="{rx}" ry="{ry}" fill="url(#sh)"/>{body}</svg>')


def hexnut(cx, cy, r, fill='url(#brass)', hole='#6E5216', hr=None):
    pts = ' '.join(f'{cx + r * math.cos(math.radians(a)):.1f},{cy + r * math.sin(math.radians(a)):.1f}' for a in range(0, 360, 60))
    hr = hr or r * .48
    return (f'<polygon points="{pts}" fill="{fill}" stroke="#7A5A18" stroke-width="3"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r * .78:.1f}" fill="none" stroke="#FFF2C4" stroke-opacity=".55" stroke-width="3"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{hr:.1f}" fill="{hole}"/><circle cx="{cx}" cy="{cy}" r="{hr * .7:.1f}" fill="#3B2C0B"/>')


def wires(x, y, colors, length=90, dx=0, spread=14):
    out = ''
    for i, c in enumerate(colors):
        xx = x + (i - (len(colors) - 1) / 2) * spread
        out += f'<path d="M{xx} {y} q{dx / 2 + (i - 1) * 8} {length * .6} {dx + (i - 1) * 18} {length}" stroke="{c}" stroke-width="7" fill="none" stroke-linecap="round"/>'
    return out


def can_cap(cx, top, w, h, label, color='url(#steel)', band='#1688D4', terminals=3):
    """cylindrical metal-can run capacitor"""
    x = cx - w / 2
    t = ''.join(f'<rect x="{cx - (terminals - 1) * 16 + i * 32 - 6}" y="{top - 26}" width="12" height="26" rx="2" fill="url(#steel)" stroke="#6B7785"/>' for i in range(terminals))
    return (t + f'<rect x="{cx - w * .34}" y="{top - 8}" width="{w * .68}" height="14" rx="5" fill="#2A3542"/>'
            f'<rect x="{x}" y="{top}" width="{w}" height="{h}" rx="16" fill="{color}" stroke="#6B7785" stroke-width="2"/>'
            f'<ellipse cx="{cx}" cy="{top}" rx="{w / 2}" ry="12" fill="#DCE3EA" stroke="#6B7785" stroke-width="2"/>'
            f'<rect x="{x}" y="{top + h * .32}" width="{w}" height="{h * .38}" fill="{band}" opacity=".92"/>'
            f'<text x="{cx}" y="{top + h * .55}" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="{min(30, w / 4.2):.0f}" fill="#FFFFFF" text-anchor="middle">{label}</text>'
            f'<text x="{cx}" y="{top + h * .55 + 24}" font-family="Arial,Helvetica,sans-serif" font-size="15" fill="#E8F4FF" text-anchor="middle">440V AC</text>')


def pcb_board(x, y, w, h, fill='url(#pcb)', relays=True, heatsink=False, chip=True, conn='#F2F2F2'):
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#0E3A24" stroke-width="3"/>'
    for i in range(7):
        yy = y + 22 + i * (h - 40) / 6
        o += f'<path d="M{x + 16} {yy:.0f} h{w * .3:.0f} l14 14 h{w * .25:.0f}" stroke="#E3C36A" stroke-opacity=".55" stroke-width="2.4" fill="none"/>'
    if chip:
        o += f'<rect x="{x + w * .42}" y="{y + h * .38}" width="{w * .2}" height="{w * .2}" rx="4" fill="#1A1F25"/>'
        o += ''.join(f'<rect x="{x + w * .42 - 7}" y="{y + h * .38 + 6 + k * 11}" width="7" height="5" fill="#C9D1D9"/><rect x="{x + w * .62}" y="{y + h * .38 + 6 + k * 11}" width="7" height="5" fill="#C9D1D9"/>' for k in range(int(w * .2 / 11)))
    if relays:
        o += f'<rect x="{x + 20}" y="{y + 20}" width="{w * .2}" height="{h * .28}" rx="5" fill="#1F6FD1"/><text x="{x + 20 + w * .1}" y="{y + 20 + h * .17}" font-family="Arial" font-size="12" fill="#fff" text-anchor="middle" font-weight="700">RELAY</text>'
        o += f'<rect x="{x + 20}" y="{y + h * .58}" width="{w * .2}" height="{h * .28}" rx="5" fill="#1F6FD1"/>'
    o += f'<circle cx="{x + w * .82}" cy="{y + h * .28}" r="{h * .13}" fill="url(#darkv)"/><circle cx="{x + w * .82}" cy="{y + h * .28}" r="{h * .05}" fill="#8592A1"/>'
    o += f'<rect x="{x + w * .72}" y="{y + h * .62}" width="{w * .2}" height="{h * .2}" rx="4" fill="#F7F7F7" stroke="#B8C2CC"/>'
    o += f'<rect x="{x + w * .4}" y="{y + h - 26}" width="{w * .28}" height="16" rx="3" fill="{conn}" stroke="#AEB9C5"/>'
    if heatsink:
        o += f'<rect x="{x + w * .68}" y="{y + 8}" width="{w * .28}" height="{h * .34}" fill="url(#steel)" stroke="#6B7785"/>'
        o += ''.join(f'<rect x="{x + w * .68 + 6 + k * 10}" y="{y + 4}" width="5" height="{h * .38}" fill="#9AA6B3"/>' for k in range(int(w * .26 / 10)))
    return o


def motor(cx, cy, r, shaft_len=70, body='url(#dark)', flange=True, label=None):
    o = ''
    if flange:
        o += f'<rect x="{cx - r - 26}" y="{cy - 10}" width="{2 * r + 52}" height="20" rx="8" fill="url(#steelv)" stroke="#6B7785"/>'
        o += f'<circle cx="{cx - r - 14}" cy="{cy}" r="5" fill="#59636E"/><circle cx="{cx + r + 14}" cy="{cy}" r="5" fill="#59636E"/>'
    o += f'<rect x="{cx - r}" y="{cy - r * 1.05}" width="{2 * r}" height="{r * 2.1}" rx="{r * .45}" fill="{body}" stroke="#0E1620" stroke-width="2"/>'
    for k in range(5):
        o += f'<rect x="{cx - r + 10}" y="{cy - r * .7 + k * r * .33}" width="{2 * r - 20}" height="5" rx="2" fill="#000" opacity=".22"/>'
    o += f'<rect x="{cx - 8}" y="{cy - r * 1.05 - shaft_len}" width="16" height="{shaft_len}" fill="url(#steel)" stroke="#6B7785"/>'
    o += f'<rect x="{cx - 8}" y="{cy - r * 1.05 - shaft_len}" width="7" height="{shaft_len}" fill="#FFFFFF" opacity=".25"/>'
    if label:
        o += f'<rect x="{cx - r * .6}" y="{cy - 18}" width="{r * 1.2}" height="36" rx="4" fill="#F4F6F8"/><text x="{cx}" y="{cy + 6}" font-family="Arial" font-weight="700" font-size="15" fill="#102C50" text-anchor="middle">{label}</text>'
    return o


def coil(x, y, w, h, rows=4, bend=True):
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#fins)" stroke="#7F8C9A" stroke-width="3"/>'
    o += f'<rect x="{x - 14}" y="{y - 6}" width="16" height="{h + 12}" rx="3" fill="url(#steelv)" stroke="#6B7785"/><rect x="{x + w - 2}" y="{y - 6}" width="16" height="{h + 12}" rx="3" fill="url(#steelv)" stroke="#6B7785"/>'
    if bend:
        for i in range(rows):
            yy = y + 14 + i * (h - 28) / max(rows - 1, 1)
            o += f'<path d="M{x + w + 14} {yy:.0f} a9 9 0 0 1 0 {(h - 28) / max(rows - 1, 1) / 2:.0f}" stroke="url(#cuh)" stroke-width="9" fill="none"/>'
            o += f'<path d="M{x - 14} {yy:.0f} a9 9 0 0 0 0 {(h - 28) / max(rows - 1, 1) / 2:.0f}" stroke="#B9653A" stroke-width="9" fill="none"/>'
    return o


def tag(text, x=24, y=438, c='#102C50'):
    return f'<text x="{x}" y="{y}" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="20" fill="{c}" opacity=".55">{text}</text>'


A = {}

# ---------- Electrical ----------
A['cap_run'] = frame(can_cap(240, 150, 150, 210, '35 MFD') + wires(240, 92, [], 0), (240, 392, 120, 20))
A['cap_fan'] = frame(f'<rect x="150" y="150" width="180" height="150" rx="22" fill="url(#whiteh)" stroke="#8D9AA8" stroke-width="3"/>'
                     f'<rect x="150" y="196" width="180" height="56" fill="#1688D4"/><text x="240" y="232" font-family="Arial" font-weight="700" font-size="28" fill="#fff" text-anchor="middle">2.5 MFD</text>'
                     + wires(240, 300, ['#1B1B1B', '#1B1B1B'], 80, 0, 26) + f'<circle cx="214" cy="380" r="7" fill="#C9D1D9"/><circle cx="266" cy="380" r="7" fill="#C9D1D9"/>', (240, 400, 110, 16))
A['cap_dual'] = frame(can_cap(240, 140, 170, 220, '45+5 MFD', band='#0E6FB3') +
                      '<text x="194" y="108" font-family="Arial" font-weight="700" font-size="14" fill="#102C50" text-anchor="middle">HERM</text><text x="240" y="108" font-family="Arial" font-weight="700" font-size="14" fill="#102C50" text-anchor="middle">C</text><text x="286" y="108" font-family="Arial" font-weight="700" font-size="14" fill="#102C50" text-anchor="middle">FAN</text>',
                      (240, 392, 130, 20))
A['cap_start'] = frame(f'<rect x="170" y="130" width="140" height="210" rx="18" fill="#1E1E22" stroke="#000" stroke-width="2"/>'
                       f'<ellipse cx="240" cy="130" rx="70" ry="14" fill="#33363C"/><rect x="170" y="200" width="140" height="70" fill="#C0392B"/>'
                       f'<text x="240" y="232" font-family="Arial" font-weight="700" font-size="22" fill="#fff" text-anchor="middle">START</text><text x="240" y="258" font-family="Arial" font-size="16" fill="#FFE3DE" text-anchor="middle">60-80 MFD</text>'
                       f'<rect x="210" y="104" width="12" height="26" fill="url(#steel)"/><rect x="258" y="104" width="12" height="26" fill="url(#steel)"/>', (240, 368, 100, 16))
A['pcb_universal'] = frame(pcb_board(70, 130, 300, 190, 'url(#pcbb)') +
                           f'<rect x="380" y="150" width="66" height="120" rx="12" fill="url(#white)" stroke="#9AA6B3" stroke-width="2"/><rect x="390" y="162" width="46" height="26" rx="4" fill="#9CD7FF"/>'
                           + ''.join(f'<circle cx="{398 + (k % 2) * 30}" cy="{206 + (k // 2) * 22}" r="7" fill="#C8D2DC"/>' for k in range(4)) +
                           '<path d="M90 320 q40 60 120 50" stroke="#1B1B1B" stroke-width="5" fill="none"/><path d="M110 320 q50 70 150 40" stroke="#E14B3B" stroke-width="5" fill="none"/>'
                           '<rect x="236" y="342" width="60" height="30" rx="6" fill="#1A1F25"/><text x="266" y="363" font-family="Arial" font-size="11" fill="#C9D1D9" text-anchor="middle">SENSOR</text>', (230, 396, 180, 18))
A['pcb_original'] = frame(pcb_board(60, 120, 360, 230, heatsink=True) +
                          '<rect x="80" y="310" width="90" height="26" rx="4" fill="#F7F7F7" stroke="#B8C2CC"/><text x="125" y="328" font-family="Arial" font-size="13" fill="#102C50" text-anchor="middle" font-weight="700">OEM</text>', (240, 396, 190, 18))
A['pcb_repair'] = frame(pcb_board(70, 130, 300, 210) +
                        '<path d="M330 120 l60 -60" stroke="#4A5868" stroke-width="12" stroke-linecap="round"/><path d="M330 120 l-22 22" stroke="url(#steel)" stroke-width="6" stroke-linecap="round"/>'
                        '<circle cx="306" cy="146" r="14" fill="#FFB74D" opacity=".9"/><circle cx="306" cy="146" r="26" fill="#FFB74D" opacity=".25"/>'
                        '<path d="M392 58 q24 -10 36 6" stroke="#B9C3CE" stroke-width="4" fill="none" opacity=".8"/>', (230, 396, 180, 18))
A['pcb_inverter'] = frame(pcb_board(56, 120, 368, 230, heatsink=True, relays=False) +
                          ''.join(f'<rect x="{90 + k * 46}" y="150" width="30" height="62" rx="15" fill="url(#darkv)"/><ellipse cx="{105 + k * 46}" cy="150" rx="15" ry="5" fill="#8592A1"/>' for k in range(3)) +
                          '<rect x="90" y="236" width="120" height="40" rx="4" fill="#1A1F25"/><text x="150" y="262" font-family="Arial" font-size="14" fill="#C9D1D9" text-anchor="middle" font-weight="700">IPM</text>', (240, 396, 190, 18))
A['sensor'] = frame('<path d="M120 300 C170 230 260 340 330 220 S400 130 420 120" stroke="#1B1B1B" stroke-width="9" fill="none"/>'
                    '<path d="M120 312 C170 242 260 352 330 232 S400 142 420 132" stroke="#E5E5E5" stroke-width="9" fill="none"/>'
                    '<rect x="64" y="286" width="64" height="30" rx="6" fill="url(#steel)" stroke="#6B7785" transform="rotate(-28 96 301)"/>'
                    '<circle cx="76" cy="320" r="13" fill="url(#steel)" stroke="#6B7785"/>'
                    '<rect x="404" y="104" width="46" height="34" rx="5" fill="#FFFFFF" stroke="#9AA6B3" stroke-width="2"/><rect x="412" y="112" width="30" height="8" fill="#D0D8E0"/>'
                    '<text x="240" y="390" font-family="Arial" font-size="18" fill="#102C50" opacity=".55" text-anchor="middle" font-weight="700">10 kΩ</text>', (240, 396, 160, 14))
A['contactor'] = frame('<rect x="140" y="110" width="200" height="250" rx="18" fill="url(#white)" stroke="#8D9AA8" stroke-width="3"/>'
                       + ''.join(f'<rect x="{164 + k * 52}" y="94" width="34" height="34" rx="4" fill="url(#steelv)" stroke="#6B7785"/><circle cx="{181 + k * 52}" cy="111" r="9" fill="#6B7785"/>'
                                 f'<rect x="{164 + k * 52}" y="342" width="34" height="34" rx="4" fill="url(#steelv)" stroke="#6B7785"/><circle cx="{181 + k * 52}" cy="359" r="9" fill="#6B7785"/>' for k in range(3)) +
                       '<rect x="180" y="180" width="120" height="76" rx="8" fill="#1F6FD1"/><text x="240" y="214" font-family="Arial" font-weight="700" font-size="20" fill="#fff" text-anchor="middle">30A</text><text x="240" y="238" font-family="Arial" font-size="14" fill="#DCEEFF" text-anchor="middle">230V COIL</text>'
                       '<rect x="214" y="270" width="52" height="24" rx="4" fill="#2A3542"/>', (240, 400, 130, 16))
A['fuse'] = frame('<rect x="110" y="200" width="260" height="70" rx="35" fill="#EAF6FF" fill-opacity=".75" stroke="#9AB6CC" stroke-width="3"/>'
                  '<path d="M150 235 q30 -22 60 0 t60 0 t60 0" stroke="#7C8896" stroke-width="3" fill="none"/>'
                  '<rect x="80" y="196" width="60" height="78" rx="8" fill="url(#steelv)" stroke="#6B7785" stroke-width="2"/><rect x="340" y="196" width="60" height="78" rx="8" fill="url(#steelv)" stroke="#6B7785" stroke-width="2"/>'
                  '<text x="240" y="320" font-family="Arial" font-weight="700" font-size="22" fill="#102C50" opacity=".6" text-anchor="middle">T3.15A 250V</text>', (240, 300, 170, 16))
A['wire'] = frame('<circle cx="230" cy="230" r="128" fill="none" stroke="#3A4654" stroke-width="34"/><circle cx="230" cy="230" r="94" fill="none" stroke="#56626F" stroke-width="30"/>'
                  '<circle cx="230" cy="230" r="62" fill="url(#white)" stroke="#9AA6B3" stroke-width="3"/><circle cx="230" cy="230" r="22" fill="#D8E0E8"/>'
                  '<path d="M330 300 q60 30 90 90" stroke="#3A4654" stroke-width="22" fill="none" stroke-linecap="round"/>'
                  + ''.join(f'<path d="M412 382 l{dx} {dy}" stroke="{c}" stroke-width="8" stroke-linecap="round"/>' for dx, dy, c in [(-6, 34, '#E14B3B'), (6, 34, '#1F6FD1'), (18, 26, '#2FA36B'), (28, 14, '#F0C419')]), (240, 400, 160, 16))

# ---------- Motors ----------
A['motor_indoor'] = frame(motor(240, 250, 92, 90, label='SPLIT') + wires(300, 330, ['#E14B3B', '#1F6FD1', '#F0C419', '#1B1B1B'], 70, 40, 10), (240, 392, 140, 18))
A['motor_outdoor'] = frame(motor(240, 250, 110, 92, label='54W') +
                           ''.join(f'<rect x="{160 + k * 160}" y="320" width="10" height="56" fill="url(#steel)"/>' for k in range(2)) +
                           wires(330, 320, ['#1B1B1B', '#E14B3B', '#1F6FD1'], 70, 50, 10), (240, 398, 160, 18))
A['motor_window'] = frame(f'<rect x="150" y="160" width="180" height="170" rx="40" fill="url(#dark)" stroke="#0E1620" stroke-width="2"/>'
                          '<rect x="40" y="236" width="110" height="16" fill="url(#steel)" stroke="#6B7785"/><rect x="330" y="236" width="110" height="16" fill="url(#steel)" stroke="#6B7785"/>'
                          '<rect x="186" y="230" width="108" height="30" rx="4" fill="#F4F6F8"/><text x="240" y="251" font-family="Arial" font-weight="700" font-size="14" fill="#102C50" text-anchor="middle">DOUBLE SHAFT</text>'
                          '<rect x="164" y="330" width="152" height="20" rx="6" fill="url(#steelv)"/>', (240, 380, 160, 16))
A['motor_swing'] = frame('<circle cx="240" cy="220" r="96" fill="url(#white)" stroke="#9AA6B3" stroke-width="3"/>'
                         '<rect x="114" y="206" width="252" height="28" rx="14" fill="url(#white)" stroke="#9AA6B3" stroke-width="3"/>'
                         '<circle cx="128" cy="220" r="8" fill="#B9C3CE"/><circle cx="352" cy="220" r="8" fill="#B9C3CE"/>'
                         '<rect x="226" y="120" width="28" height="44" rx="4" fill="#E3E8EE" stroke="#9AA6B3"/><rect x="236" y="104" width="8" height="22" fill="#FFFFFF" stroke="#9AA6B3"/>'
                         '<text x="240" y="262" font-family="Arial" font-weight="700" font-size="16" fill="#102C50" text-anchor="middle" opacity=".7">12V DC</text>'
                         + wires(240, 316, ['#E14B3B', '#F0C419', '#FF8A1F', '#1F6FD1', '#E879B9'], 60, 30, 9) + '<rect x="248" y="372" width="56" height="18" rx="3" fill="#FFFFFF" stroke="#9AA6B3"/>', (240, 400, 130, 14))
A['fan_blade'] = frame('<g transform="translate(240 230)">' + ''.join(
    f'<path d="M0 0 C30 -40 120 -60 150 -10 C130 20 60 30 0 0Z" fill="#2A3542" transform="rotate({a})" stroke="#111A24" stroke-width="2"/>' for a in (0, 120, 240)) +
                       '<circle r="36" fill="url(#darkv)" stroke="#111A24" stroke-width="3"/><circle r="12" fill="url(#steel)"/></g>', (240, 410, 150, 16))
A['swing_blade'] = frame('<path d="M40 240 C150 200 330 200 440 240 L440 268 C330 236 150 236 40 268Z" fill="url(#white)" stroke="#9AA6B3" stroke-width="3"/>'
                         '<path d="M60 262 C160 232 320 232 420 262" stroke="#FFFFFF" stroke-width="5" fill="none"/>'
                         '<rect x="56" y="230" width="22" height="34" rx="4" fill="#E3E8EE" stroke="#9AA6B3"/><rect x="402" y="230" width="22" height="34" rx="4" fill="#E3E8EE" stroke="#9AA6B3"/>'
                         '<rect x="226" y="214" width="28" height="22" rx="4" fill="#E3E8EE" stroke="#9AA6B3"/>', (240, 320, 200, 16))
A['blower_wheel'] = frame('<g transform="rotate(-14 240 240)"><rect x="40" y="170" width="400" height="140" rx="20" fill="#E9EEF3" stroke="#8D9AA8" stroke-width="3"/>'
                          + ''.join(f'<rect x="{50 + k * 13}" y="174" width="5" height="132" fill="#9DA9B6"/>' for k in range(30)) +
                          ''.join(f'<rect x="{38 + k * 100}" y="166" width="10" height="148" rx="4" fill="#C3CDD7" stroke="#8D9AA8"/>' for k in range(5)) +
                          '<ellipse cx="440" cy="240" rx="18" ry="70" fill="#D5DDE5" stroke="#8D9AA8" stroke-width="3"/><circle cx="452" cy="240" r="12" fill="url(#darkv)"/></g>', (240, 380, 200, 16))

# ---------- Refrigeration ----------
def compressor_svg(color='url(#dark)', label='', badge=None):
    o = (f'<rect x="130" y="330" width="220" height="26" rx="8" fill="url(#darkv)"/>'
         f'<rect x="150" y="120" width="180" height="230" rx="80" fill="{color}" stroke="#0E1620" stroke-width="2"/>'
         f'<ellipse cx="240" cy="128" rx="88" ry="32" fill="#4E5B6A" opacity=".6"/>'
         f'<path d="M330 200 h50 v-70" stroke="url(#cuh)" stroke-width="16" fill="none" stroke-linecap="round"/>'
         f'<path d="M330 252 h70 v-150" stroke="#B9653A" stroke-width="11" fill="none" stroke-linecap="round"/>'
         f'<rect x="160" y="196" width="42" height="56" rx="8" fill="#2A3542" stroke="#111A24"/>')
    if label:
        o += f'<rect x="196" y="270" width="88" height="34" rx="5" fill="#F4F6F8"/><text x="240" y="293" font-family="Arial" font-weight="700" font-size="16" fill="#102C50" text-anchor="middle">{label}</text>'
    if badge:
        o += f'<rect x="300" y="300" width="130" height="40" rx="20" fill="#E9761A"/><text x="365" y="327" font-family="Arial" font-weight="700" font-size="17" fill="#fff" text-anchor="middle">{badge}</text>'
    return o

A['compressor'] = frame(compressor_svg('url(#dark)', 'R32 / R22'), (240, 380, 140, 18))
A['compressor_inv'] = frame(compressor_svg('url(#pcbb)', 'BLDC'), (240, 380, 140, 18))
A['compressor_refurb'] = frame(compressor_svg('url(#darkv)', 'BLDC', 'REFURB'), (240, 380, 140, 18))
A['coil_condenser'] = frame('<g transform="translate(0 6)">' + coil(80, 120, 320, 240, 5) + '</g>'
                            '<path d="M60 150 h-20 v40" stroke="url(#cuh)" stroke-width="14" fill="none" stroke-linecap="round"/>', (240, 400, 190, 16))
A['coil_evap'] = frame('<path d="M60 300 L240 140 L420 300" fill="none" stroke="#7F8C9A" stroke-width="3"/>'
                       '<path d="M70 300 L240 150 L240 330 L70 330Z" fill="url(#fins)" stroke="#7F8C9A" stroke-width="3"/><path d="M240 150 L410 300 L410 330 L240 330Z" fill="url(#fins)" stroke="#7F8C9A" stroke-width="3"/>'
                       + ''.join(f'<circle cx="{410}" cy="{300 + k * 0}" r="0"/>' for k in range(1)) +
                       ''.join(f'<path d="M{412} {196 + k * 34} a10 10 0 0 1 0 17" stroke="url(#cuh)" stroke-width="8" fill="none"/>' for k in range(4)) +
                       '<path d="M410 330 v40 h30" stroke="url(#cuh)" stroke-width="12" fill="none" stroke-linecap="round"/><path d="M380 330 v52 h60" stroke="#B9653A" stroke-width="8" fill="none" stroke-linecap="round"/>', (240, 400, 190, 16))
A['exp_valve'] = frame('<rect x="190" y="90" width="100" height="120" rx="14" fill="url(#dark)" stroke="#0E1620" stroke-width="2"/>'
                       '<text x="240" y="158" font-family="Arial" font-weight="700" font-size="16" fill="#C9D1D9" text-anchor="middle">EEV</text>'
                       '<rect x="208" y="210" width="64" height="90" rx="8" fill="url(#brassv)" stroke="#7A5A18" stroke-width="2"/>'
                       '<path d="M208 260 h-110" stroke="url(#cu)" stroke-width="18" stroke-linecap="round"/><path d="M240 300 v80" stroke="url(#cuh)" stroke-width="18" stroke-linecap="round"/>'
                       + wires(290, 120, ['#E14B3B', '#F0C419', '#1F6FD1', '#1B1B1B'], 70, 70, 8), (240, 400, 140, 16))
A['capillary'] = frame(''.join(f'<ellipse cx="200" cy="230" rx="{120 - k * 14}" ry="{120 - k * 14}" fill="none" stroke="url(#cu)" stroke-width="6"/>' for k in range(5)) +
                       '<rect x="300" y="150" width="140" height="44" rx="22" fill="url(#cuh)" stroke="#8A3E1C" stroke-width="2"/>'
                       '<path d="M300 172 h-20 q-20 0 -30 20" stroke="#B9653A" stroke-width="6" fill="none"/><path d="M440 172 h20" stroke="#B9653A" stroke-width="10"/>'
                       '<text x="360" y="232" font-family="Arial" font-weight="700" font-size="15" fill="#102C50" opacity=".6" text-anchor="middle">FILTER DRIER</text>', (240, 392, 170, 16))
A['service_valve'] = frame('<rect x="180" y="150" width="120" height="150" rx="12" fill="url(#brass)" stroke="#7A5A18" stroke-width="3"/>'
                           '<rect x="300" y="196" width="70" height="40" rx="6" fill="url(#brassv)" stroke="#7A5A18" stroke-width="2"/>' + hexnut(390, 216, 34) +
                           '<rect x="210" y="100" width="60" height="56" rx="6" fill="url(#brassv)" stroke="#7A5A18" stroke-width="2"/><circle cx="240" cy="96" r="20" fill="url(#brass)" stroke="#7A5A18" stroke-width="2"/>'
                           '<rect x="140" y="220" width="40" height="34" rx="4" fill="url(#brassv)" stroke="#7A5A18" stroke-width="2"/>'
                           '<path d="M240 300 v40 q0 40 -40 40 h-110" stroke="url(#cu)" stroke-width="22" fill="none" stroke-linecap="round"/>', (240, 400, 170, 16))
A['flare_nut'] = frame('<g transform="translate(-60 0)">' + hexnut(230, 230, 96) + '</g>'
                       '<g transform="translate(120 70)">' + hexnut(230, 230, 58) + '</g>', (240, 380, 180, 18))
A['pin_valve'] = frame('<rect x="140" y="220" width="210" height="34" rx="6" fill="url(#brassv)" stroke="#7A5A18" stroke-width="2"/>'
                       + ''.join(f'<rect x="{150 + k * 14}" y="220" width="4" height="34" fill="#9A7322" opacity=".6"/>' for k in range(10)) +
                       '<rect x="350" y="228" width="70" height="18" rx="3" fill="url(#steel)" stroke="#6B7785"/><rect x="420" y="232" width="20" height="10" fill="url(#steel)"/>'
                       '<path d="M140 237 h-60" stroke="#6E5216" stroke-width="10" stroke-linecap="round"/>'
                       '<circle cx="120" cy="330" r="34" fill="#C62828"/><rect x="104" y="296" width="32" height="20" fill="#C62828"/><text x="120" y="338" font-family="Arial" font-weight="700" font-size="16" fill="#fff" text-anchor="middle">CAP</text>', (260, 380, 170, 14))

# ---------- Installation & accessories ----------
A['copper_pipe'] = frame(''.join(f'<ellipse cx="240" cy="240" rx="{150 - k * 12}" ry="{110 - k * 9}" fill="none" stroke="url(#cu)" stroke-width="14"/>' for k in range(6)) +
                         '<path d="M370 280 q50 30 70 90" stroke="url(#cuh)" stroke-width="14" fill="none" stroke-linecap="round"/><ellipse cx="440" cy="372" rx="8" ry="6" fill="#5A2A12"/>', (240, 380, 180, 16))
A['copper_set'] = frame('<path d="M60 300 C140 160 300 380 420 170" stroke="url(#foam)" stroke-width="44" fill="none" stroke-linecap="round"/>'
                        '<path d="M60 360 C150 230 300 430 420 240" stroke="url(#foam)" stroke-width="30" fill="none" stroke-linecap="round"/>'
                        '<path d="M70 392 C160 270 300 450 420 280" stroke="#3A4654" stroke-width="10" fill="none" stroke-linecap="round"/>'
                        '<path d="M420 170 l30 -24" stroke="url(#cuh)" stroke-width="16" stroke-linecap="round"/><path d="M420 240 l26 -18" stroke="url(#cuh)" stroke-width="11" stroke-linecap="round"/>', (240, 420, 190, 14))
A['drain_pipe'] = frame('<path d="M50 140 C150 140 160 320 260 320 S380 190 430 260" stroke="#DDE4EB" stroke-width="40" fill="none" stroke-linecap="round"/>'
                        '<path d="M50 140 C150 140 160 320 260 320 S380 190 430 260" stroke="#AEBBC8" stroke-width="40" fill="none" stroke-dasharray="4 10" stroke-linecap="butt"/>'
                        '<circle cx="430" cy="260" r="16" fill="#8592A1"/><path d="M432 292 q4 18 0 30" stroke="#56C8FF" stroke-width="6" fill="none" stroke-linecap="round"/>', (240, 390, 190, 16))
A['bracket'] = frame('<path d="M110 100 v260 M110 340 L360 340 M110 120 L360 330" stroke="url(#steelv)" stroke-width="26" stroke-linecap="square" fill="none"/>'
                     '<path d="M110 100 v260 M110 340 L360 340 M110 120 L360 330" stroke="#6B7785" stroke-width="2" fill="none" opacity=".6"/>'
                     + ''.join(f'<circle cx="110" cy="{140 + k * 70}" r="7" fill="#46515D"/>' for k in range(3)) +
                     ''.join(f'<ellipse cx="{200 + k * 110}" cy="326" rx="18" ry="7" fill="#1B1B1B"/>' for k in range(2)), (240, 380, 160, 16))
A['remote'] = frame('<rect x="170" y="70" width="140" height="330" rx="44" fill="url(#white)" stroke="#9AA6B3" stroke-width="3"/>'
                    '<rect x="190" y="100" width="100" height="74" rx="8" fill="#BFE6FF" stroke="#7FA8C4"/>'
                    '<text x="240" y="152" font-family="Arial" font-weight="700" font-size="36" fill="#102C50" text-anchor="middle">24°</text>'
                    '<circle cx="240" cy="210" r="18" fill="#E53935"/><circle cx="240" cy="210" r="7" fill="none" stroke="#fff" stroke-width="2.5"/>'
                    + ''.join(f'<rect x="{196 + (k % 3) * 32}" y="{244 + (k // 3) * 34}" width="24" height="22" rx="7" fill="#D2DAE3"/>' for k in range(9)), (240, 410, 100, 14))
A['remote_pcb'] = frame('<g transform="translate(-60 0)"><rect x="150" y="80" width="120" height="290" rx="38" fill="url(#white)" stroke="#9AA6B3" stroke-width="3"/>'
                        '<rect x="168" y="106" width="84" height="60" rx="7" fill="#BFE6FF"/><circle cx="210" cy="196" r="15" fill="#E53935"/>'
                        + ''.join(f'<rect x="{172 + (k % 3) * 28}" y="{226 + (k // 3) * 30}" width="20" height="18" rx="6" fill="#D2DAE3"/>' for k in range(9)) + '</g>'
                        + pcb_board(260, 180, 180, 120, relays=False, chip=True) +
                        '<circle cx="290" cy="210" r="12" fill="#1A1F25"/><circle cx="290" cy="210" r="5" fill="#6E3AC8"/>', (240, 400, 180, 14))
A['water_tray'] = frame('<path d="M50 190 L430 190 L400 320 L80 320Z" fill="url(#white)" stroke="#9AA6B3" stroke-width="3"/>'
                        '<path d="M70 200 L410 200 L388 300 L92 300Z" fill="#E6EEF5"/>'
                        '<path d="M110 280 q60 -12 120 0 t120 0" stroke="#7DD3FC" stroke-width="10" fill="none" opacity=".8"/>'
                        '<rect x="410" y="250" width="36" height="22" rx="6" fill="#D2DAE3" stroke="#9AA6B3"/>', (240, 360, 200, 16))
A['filter'] = frame('<g transform="rotate(-6 240 240)"><rect x="90" y="90" width="300" height="300" rx="22" fill="url(#white)" stroke="#9AA6B3" stroke-width="3"/>'
                    '<rect x="112" y="112" width="256" height="256" rx="10" fill="url(#mesh)"/>'
                    '<rect x="112" y="234" width="256" height="12" fill="#D2DAE3"/><rect x="234" y="112" width="12" height="256" fill="#D2DAE3"/>'
                    '<rect x="210" y="84" width="60" height="22" rx="8" fill="#D2DAE3" stroke="#9AA6B3"/></g>', (240, 410, 170, 16))
A['coil_cleaner'] = frame('<rect x="180" y="140" width="120" height="240" rx="18" fill="url(#blue)" stroke="#0E5A92" stroke-width="2"/>'
                          '<rect x="180" y="210" width="120" height="96" fill="#FFFFFF"/><text x="240" y="250" font-family="Arial" font-weight="700" font-size="19" fill="#102C50" text-anchor="middle">COIL</text><text x="240" y="276" font-family="Arial" font-weight="700" font-size="17" fill="#1688D4" text-anchor="middle">CLEANER</text>'
                          '<rect x="196" y="112" width="88" height="34" rx="8" fill="url(#steelv)"/><rect x="210" y="74" width="56" height="44" rx="8" fill="#FFFFFF" stroke="#9AA6B3" stroke-width="2"/>'
                          '<rect x="264" y="86" width="40" height="12" rx="4" fill="#FFFFFF" stroke="#9AA6B3"/>'
                          + ''.join(f'<circle cx="{330 + (k % 3) * 22}" cy="{92 + (k // 3) * 20 - (k % 3) * 6}" r="{9 - k % 3 * 2}" fill="#FFFFFF" stroke="#BFE6FF" stroke-width="2"/>' for k in range(6)), (240, 392, 100, 16))
A['anti_rust'] = frame('<rect x="40" y="150" width="210" height="190" fill="url(#fins)" stroke="#7F8C9A" stroke-width="3"/>'
                       '<rect x="40" y="150" width="120" height="190" fill="#7FBF7F" opacity=".35"/>'
                       '<rect x="260" y="150" width="110" height="230" rx="16" fill="url(#orange)" stroke="#B4560E" stroke-width="2"/>'
                       '<rect x="260" y="220" width="110" height="80" fill="#FFFFFF"/><text x="315" y="256" font-family="Arial" font-weight="700" font-size="17" fill="#102C50" text-anchor="middle">ANTI</text><text x="315" y="280" font-family="Arial" font-weight="700" font-size="17" fill="#E9761A" text-anchor="middle">RUST</text>'
                       '<rect x="276" y="120" width="78" height="34" rx="8" fill="url(#steelv)"/><rect x="290" y="88" width="50" height="38" rx="8" fill="#1B1B1B"/>'
                       '<path d="M284 104 l-60 30" stroke="#B9E0B9" stroke-width="22" stroke-linecap="round" opacity=".55"/>', (220, 400, 180, 16))


def build(only=None, outdir='static/assets/img/parts', srcdir='art-src/parts'):
    os.makedirs(outdir, exist_ok=True); os.makedirs(srcdir, exist_ok=True)
    for k, svgtxt in A.items():
        if only and k not in only: continue
        sp = os.path.join(srcdir, k + '.svg'); open(sp, 'w').write(svgtxt)
        png = f'/tmp/part_{k}.png'
        subprocess.run(['rsvg-convert', '-w', str(W), sp, '-o', png], check=True)
        Image.open(png).convert('RGB').save(os.path.join(outdir, k + '.webp'), quality=84, method=6)
    print('built', len(only or A), 'part images')


if __name__ == '__main__':
    build(sys.argv[1:] or None)
