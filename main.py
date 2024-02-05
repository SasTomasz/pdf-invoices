import os
from datetime import datetime

import pandas as pd
from fpdf import FPDF


def add_cell(product_id, product_name, amount, price, total_price):
    pdf.cell(30, 10, product_id, 1, 0)
    pdf.cell(70, 10, product_name, 1, 0)
    pdf.cell(30, 10, amount, 1, 0)
    pdf.cell(30, 10, price, 1, 0)
    pdf.cell(30, 10, total_price, 1, 1)


files = os.listdir("./input")
for f in files:
    df = pd.read_excel(f"./input/{f}")

    generate_date = datetime.now().strftime("%Y.%m.%d")
    pdf = FPDF()
    col_product_id = "Product ID"
    col_product_name = "Product Name"
    col_amount = "Amount"
    col_price = "Price per Unit"
    col_total_price = "Total Price"
    title = "Invoice nr. 10001"
    date = f"Date {generate_date}"
    total_price_value = 0

    # Draw a pdf
    pdf.add_page()
    pdf.set_font("Times", "B", 22)
    pdf.cell(0, 10, title, 0, 1)
    pdf.cell(0, 10, date, ln=1)
    pdf.ln()
    pdf.set_font("Times", "B", 12)
    add_cell(col_product_id, col_product_name, col_amount, col_price, col_total_price)
    pdf.set_font("Times", "", 12)

    for index, row in df.iterrows():
        col_product_id = str(row['product_id'])
        col_product_name = row['product_name']
        col_amount = str(row['amount_purchased'])
        col_price = str(row['price_per_unit'])
        col_total_price = str(row['total_price'])
        total_price_value += row['total_price']
        add_cell(col_product_id, col_product_name, col_amount, col_price, col_total_price)

    add_cell("", "", "", "", str(total_price_value))

    pdf.set_font("Times", "B", 12)
    pdf.ln(20)
    summary = f"The total due amount is {total_price_value} Euros"
    pdf.cell(0, 10, summary, 0, 1)

    file_name = f.strip(".xlsx") + ".pdf"
    pdf.output(f"./output/{file_name}")

