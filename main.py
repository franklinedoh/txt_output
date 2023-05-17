import glob
from fpdf import FPDF
from pathlib import Path
#import pandas as pd

filepaths = glob.glob("textfiles/*.txt")
print(filepaths)
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    heading = Path(filepath).stem
    name = heading.title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f'{name}', ln=1)

    with open(filepath, 'r') as file:
        content = file.read()
        pdf.set_font(family="Times", size=12)
        pdf.multi_cell(w=0, h=8, txt=content)

pdf.output("new.pdf")

