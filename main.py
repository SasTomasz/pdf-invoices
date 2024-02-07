import os
from datetime import datetime

import pandas as pd
from fpdf import FPDF


def add_cell(product_id, product_name, amount, price, total_price):
    args = locals()
    for i in args.items():
        if i[0] == "product_name":
            pdf.cell(70, 10, i[1], 1, 0)
        elif i[0] == "total_price":
            pdf.cell(30, 10, i[1], 1, 1)
        else:
            pdf.cell(30, 10, i[1], 1, 0)


files = os.listdir("./input")
for f in files:
    df = pd.read_excel(f"./input/{f}")
    number_and_date = f.split("-")

    generate_date = datetime.now().strftime("%Y.%m.%d")
    pdf = FPDF()
    col_product_id = "Product ID"
    col_product_name = "Product Name"
    col_amount = "Amount"
    col_price = "Price per Unit"
    col_total_price = "Total Price"
    title = f"Invoice nr {number_and_date[0]}"
    label_generate_date = f"Date of generate: {generate_date}"
    label_document_date = f"Document Date: {number_and_date[1]}"
    total_price_value = 0

    # Draw a pdf
    pdf.add_page()
    pdf.set_font("Times", "B", 22)
    pdf.cell(0, 10, title, 0, 1)
    pdf.cell(0, 10, label_generate_date, ln=1)
    pdf.cell(0, 10, label_document_date.strip(".xlsx"), ln=1)
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

# TODO:
#  * Use pathlib and glob

