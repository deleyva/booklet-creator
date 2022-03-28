from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj
import sys
import os

if len(sys.argv) != 2 or ".pdf" not in sys.argv[1].lower():
    print(f"Usage: python {sys.argv[0]} <pdf filename>")
    sys.exit()
input_file = sys.argv[1]
output_file = f'{os.path.splitext(sys.argv[1])[0]}_pgn.pdf'
print(output_file)

reader = PdfReader(input_file)
pages = [pagexobj(p) for p in reader.pages]

canvas = Canvas(output_file, pagesize=(pages[0].BBox[2], pages[0].BBox[3]))

for page_num, page in enumerate(pages, start=1):
    canvas.doForm(makerl(canvas, page))

    footer_text = f"{page_num}/{len(pages)}"
    canvas.saveState()
    canvas.setStrokeColorRGB(0, 0, 0)
    canvas.setFont('Times-Roman', 14)
    canvas.drawString(290, 10, footer_text)
    canvas.restoreState()
    canvas.showPage()

canvas.save()
