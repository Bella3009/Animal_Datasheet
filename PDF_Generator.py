import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    df = pd.read_csv(filepath)
    pdf.add_page()
    filename = Path(filepath).stem
    animal = filename.title()
    with open(filepath, "r") as file:
        content = file.read()
    
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=0, h=20, txt=animal, ln=1)
    pdf.line(10, 25, 200, 25)
    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=0, h=2, txt=content)
    
pdf.output(f"Animals.pdf")
