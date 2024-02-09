from glob import glob
from datetime import datetime
from pathlib import Path

import pandas as pd
from fpdf import FPDF


def add_cell(product_id, product_name, amount, price, total_price):
    pdf.cell(20, 10, product_id, 1, 0)
    pdf.cell(60, 10, product_name, 1, 0)
    pdf.cell(35, 10, amount, 1, 0)
    pdf.cell(30, 10, price, 1, 0)
    pdf.cell(30, 10, total_price, 1, 1)


files = glob("./input/*xlsx")
for f in files:
    df = pd.read_excel(f)
    invoice_number, invoice_date = Path(f).stem.split("-")
    columns = df.columns

    generate_date = datetime.now().strftime("%Y.%m.%d")
    pdf = FPDF()
    col_product_id = str(columns[0]).replace("_", " ").title()
    col_product_name = str(columns[1]).replace("_", " ").title()
    col_amount = str(columns[2]).replace("_", " ").title()
    col_price = str(columns[3]).replace("_", " ").title()
    col_total_price = str(columns[4]).replace("_", " ").title()
    title = f"Invoice nr {invoice_number}"
    label_generate_date = f"Date of generate: {generate_date}"
    label_document_date = f"Document Date: {invoice_date}"
    total_price_value = 0

    # Draw a pdf
    pdf.add_page()
    pdf.set_font("Times", "B", 22)
    pdf.cell(0, 10, title, 0, 1)
    pdf.cell(0, 10, label_generate_date, ln=1)
    pdf.cell(0, 10, label_document_date, ln=1)
    pdf.ln()
    pdf.set_font("Times", "B", 10)
    add_cell(col_product_id, col_product_name, col_amount, col_price, col_total_price)
    pdf.set_font("Times", "", 10)

    for index, row in df.iterrows():
        col_product_id = str(row['product_id'])
        col_product_name = row['product_name']
        col_amount = str(row['amount_purchased'])
        col_price = str(row['price_per_unit'])
        col_total_price = str(row['total_price'])
        add_cell(col_product_id, col_product_name, col_amount, col_price, col_total_price)

    total_price_value = sum(df['total_price'])
    add_cell("", "", "", "", str(total_price_value))

    pdf.set_font("Times", "B", 12)
    pdf.ln(20)
    summary = f"The total due amount is {total_price_value} Euros"
    pdf.cell(0, 10, summary, 0, 1)

    file_name = str(Path(f).stem) + ".pdf"
    pdf.output(f"./output/{file_name}")
