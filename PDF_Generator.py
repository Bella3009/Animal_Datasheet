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
    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=0, h=2, txt=animal)
    
pdf.output(f"Animals.pdf")
