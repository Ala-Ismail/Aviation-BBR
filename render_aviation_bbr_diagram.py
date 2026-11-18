"""Render the Aviation BBR reference scenario as editable SVG and PNG.

Run from the repository root: python render_aviation_bbr_diagram.py
Rendering uses Pillow and the Windows Segoe UI fonts.
"""

from pathlib import Path
import math
import xml.etree.ElementTree as ET

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parent / "images"
OUT.mkdir(exist_ok=True)
WIDTH, HEIGHT = 1800, 1080
SCALE = 2
NAVY, TEAL, AMBER = "#23435b", "#087e8b", "#aa640e"
TEXT, MUTED = "#183349", "#526b7e"
SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)
root = ET.Element(f"{{{SVG}}}svg", {
    "width": str(WIDTH), "height": str(HEIGHT),
    "viewBox": f"0 0 {WIDTH} {HEIGHT}", "role": "img",
    "aria-labelledby": "title description",
})
ET.SubElement(root, f"{{{SVG}}}title", {"id": "title"}).text = "Aviation BBR technology assessment: FPGA recorder reference scenario"
ET.SubElement(root, f"{{{SVG}}}desc", {"id": "description"}).text = (
    "Aircraft instrument data enters acquisition, scheduled queues and a chunk framer "
    "inside a MAX 10 10M50 FPGA. The storage controller writes mirrored F-RAM staging "
    "outside the candidate crash enclosure and a 32 GiB raw NAND archive inside it. "
    "The last data held in staging could be lost at impact. The architecture and "
    "capacity assumptions are used for comparison in the technology assessment."
)
canvas = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), "#f4f7fb")
draw = ImageDraw.Draw(canvas)
font_dir = Path("C:/Windows/Fonts")


def element(tag, **attrs):
    return ET.SubElement(root, f"{{{SVG}}}{tag}", {k.replace("_", "-"): str(v) for k, v in attrs.items()})


def text(x, y, value, size=19, bold=False, color=TEXT, anchor="start"):
    element("text", x=x, y=y, fill=color, font_size=size,
            font_family="Segoe UI, Arial, sans-serif", font_weight=700 if bold else 400,
            text_anchor=anchor).text = value
    font = ImageFont.truetype(str(font_dir / ("segoeuib.ttf" if bold else "segoeui.ttf")), size * SCALE)
    draw.text((x * SCALE, y * SCALE), value, font=font, fill=color,
              anchor={"start": "ls", "middle": "ms", "end": "rs"}[anchor])


def rect(x, y, width, height, fill, stroke="#d2dde7", radius=16, dashed=False):
    attrs = dict(x=x, y=y, width=width, height=height, rx=radius,
                 fill=fill, stroke=stroke, stroke_width=2)
    if dashed:
        attrs["stroke_dasharray"] = "8 6"
    element("rect", **attrs)
    draw.rounded_rectangle((x*SCALE, y*SCALE, (x+width)*SCALE, (y+height)*SCALE),
                           radius=radius*SCALE, fill=fill, outline=stroke, width=2*SCALE)


def box(x, y, width, height, heading, lines, fill="#ffffff", stroke="#d2dde7"):
    rect(x, y, width, height, fill, stroke)
    def fitted_size(value, initial, bold=False):
        size = initial
        while size > 13:
            font = ImageFont.truetype(str(font_dir / ("segoeuib.ttf" if bold else "segoeui.ttf")), size*SCALE)
            if font.getlength(value) <= (width-36)*SCALE:
                return size
            size -= 1
        raise ValueError(f"Label does not fit: {value}")

    text(x+18, y+34, heading, fitted_size(heading, 21, True), True)
    for index, line in enumerate(lines):
        text(x+18, y+66+index*27, line, fitted_size(line, 18), color=MUTED)


def line(points, color=NAVY, dashed=False, both=False):
    attrs = dict(points=" ".join(f"{x},{y}" for x, y in points), fill="none",
                 stroke=color, stroke_width=3, stroke_linejoin="round")
    if dashed:
        attrs["stroke_dasharray"] = "8 6"
    element("polyline", **attrs)
    for start, end in zip(points, points[1:]):
        length = math.dist(start, end)
        if dashed:
            for offset in range(0, int(length), 14):
                a, b = offset/length, min(offset+8, length)/length
                p = (start[0]+(end[0]-start[0])*a, start[1]+(end[1]-start[1])*a)
                q = (start[0]+(end[0]-start[0])*b, start[1]+(end[1]-start[1])*b)
                draw.line([(v[0]*SCALE, v[1]*SCALE) for v in [p, q]], fill=color, width=3*SCALE)
        else:
            draw.line([(v[0]*SCALE, v[1]*SCALE) for v in [start, end]], fill=color, width=3*SCALE)
    arrow(points[-2], points[-1], color)
    if both:
        arrow(points[1], points[0], color)


def arrow(previous, tip, color):
    angle = math.atan2(tip[1]-previous[1], tip[0]-previous[0])
    back = (tip[0]-12*math.cos(angle), tip[1]-12*math.sin(angle))
    corners = [tip, (back[0]+5*math.sin(angle), back[1]-5*math.cos(angle)),
               (back[0]-5*math.sin(angle), back[1]+5*math.cos(angle))]
    element("polygon", points=" ".join(f"{x},{y}" for x, y in corners), fill=color)
    draw.polygon([(x*SCALE, y*SCALE) for x, y in corners], fill=color)


rect(0, 0, WIDTH, HEIGHT, "#f4f7fb", "#f4f7fb", 0)
text(40, 57, "AVIATION BBR", 34, True)
text(40, 91, "FPGA reference scenario for continuous instrument recording", 23, color=MUTED)
text(1760, 54, "TECHNOLOGY ASSESSMENT", 17, True, TEAL, "end")
text(1760, 84, "8 November 2026  |  Research baseline", 16, color=MUTED, anchor="end")

rect(400, 130, 850, 800, "#eaf2fa", "#8daec9", 22)
text(430, 168, "FPGA  ·  MAX 10 10M50DAF484I7G", 25, True)
text(430, 199, "Sizing assumptions: 75 MHz core, 30,000 fitted LEs, 182 M9Ks available", 18, color=MUTED)
rect(1280, 445, 480, 255, "#e9f6ee", "#529d70", 20)
text(1300, 476, "CANDIDATE CRASH ENCLOSURE", 17, True, "#287146")

box(40, 235, 300, 160, "Aircraft instrument data", [
    "Air data, attitude, navigation", "Engines, controls, warnings", "Via bus / ADC front ends"], "#ffffff")
box(40, 435, 300, 120, "External time service", ["Coherent time / valid / ticks", "Owns time synchronization"])
box(40, 635, 300, 120, "Aircraft power / state", ["Power-good, reset, flight state", "Supervised supply to all blocks"])
box(40, 785, 300, 100, "DSP / maintenance host", ["Commands, status, downloads"])

box(440, 235, 230, 160, "Acquisition adapters", ["Parameter / source IDs", "Input timestamps", "Validity and source age"])
box(710, 235, 190, 160, "Scheduled queues", ["Per-parameter rates", "Bounded FIFOs", "Loss / gap tracking"])
box(940, 235, 270, 160, "Continuous chunk framer", ["Versioned records and CRC", "Sequence / time / quality", "Short recoverable chunks"])
box(440, 475, 230, 150, "Recording control", ["Automatic flight operation", "Preservation / safe commands", "Optional event markers"], "#fff6e8", "#dfbb7c")
box(710, 475, 190, 150, "Health supervisor", ["Recorder self-checks", "Time / queue faults", "Media / power faults"], "#fff6e8", "#dfbb7c")
box(940, 475, 270, 150, "Storage / recovery", ["Mirrored F-RAM transactions", "NAND / ECC / bad blocks", "Commit and restart recovery"], "#e7f6f7", "#76b9bd")
box(440, 740, 460, 130, "Host interface and controlled readout", [
    "Recording-priority arbitration and status", "Schema-aware instrument data export"], "#ffffff")

box(1300, 235, 440, 170, "Mirrored F-RAM staging", [
    "2 × 16 Mbit, 2 MiB logical after mirroring", "1.5 MiB data, 0.5 MiB metadata reserve", "≈ 9 s at modeled rate from empty", "Data held outside the crash enclosure"], "#e7f6f7", "#76b9bd")
box(1300, 500, 440, 175, "NAND archive", [
    "32 GiB raw, 16 GiB assumed usable", "25-hour retention scenario", "Media, ECC and service limits open", "Modeled stream: 175,000 bytes/s"], "#ffffff", "#83b698")
box(1300, 740, 440, 130, "Independent recovery / ground tools", [
    "Documented media format and separate decoder", "Recover data without the normal DSP host"], "#ffffff")

line([(340, 290), (440, 290)])
line([(670, 315), (710, 315)])
line([(900, 315), (940, 315)])
line([(1075, 395), (1075, 475)])
text(1090, 440, "chunk stream", 16, color=MUTED)
line([(1210, 525), (1260, 525), (1260, 330), (1300, 330)], TEAL, both=True)
line([(1210, 585), (1300, 585)], TEAL, both=True)
line([(340, 495), (380, 495), (380, 365), (440, 365)], AMBER, True)
line([(555, 475), (555, 395)], AMBER, True)
line([(805, 395), (805, 475)], AMBER, True)
line([(710, 550), (670, 550)], AMBER, True)
line([(900, 550), (940, 550)], AMBER, True, both=True)
line([(340, 695), (805, 695), (805, 625)], AMBER, True)
line([(340, 825), (440, 825)], TEAL, both=True)
line([(555, 740), (555, 625)], AMBER, True)
text(570, 678, "commands / status", 16, color=MUTED)
line([(900, 800), (1075, 800), (1075, 625)], TEAL, both=True)
text(938, 833, "readout / recovery", 16, color=MUTED)
line([(1520, 675), (1520, 740)], TEAL)
text(1535, 720, "service extraction", 16, color=MUTED)

line([(40, 960), (110, 960)])
text(125, 967, "Instrument data", 17)
line([(330, 960), (400, 960)], TEAL, both=True)
text(415, 967, "Storage / readout", 17)
line([(655, 960), (725, 960)], AMBER, True)
text(740, 967, "Control / time / health", 17)
text(1760, 967, "Independent extraction interface remains open.", 15, color=MUTED, anchor="end")
text(40, 1016, "CAPACITY MODEL", 16, True, TEAL)
text(250, 1016, "140,000 B/s + 25% allowance = 175,000 B/s. At that rate, 16 GiB usable holds about 27.3 h.", 18)
text(40, 1050, "Open feasibility questions: repeated media stalls, data held in staging at impact, FPGA and board fit, and aircraft qualification.", 17, color=MUTED)

ET.indent(root)
ET.ElementTree(root).write(OUT / "aviation-bbr-top-level.svg", encoding="utf-8", xml_declaration=True)
canvas.save(OUT / "aviation-bbr-top-level.png", optimize=True)
print(f"Created {OUT / 'aviation-bbr-top-level.svg'}")
print(f"Created {OUT / 'aviation-bbr-top-level.png'}")
