from fpdf import FPDF
import pandas
from datetime import datetime


def add_cell(product_id, product_name, amount, price, total_price):
    pdf.set_font("Times", "", 12)
    pdf.cell(30, 10, product_id, 1, 0)
    pdf.cell(70, 10, product_name, 1, 0)
    pdf.cell(30, 10, amount, 1, 0)
    pdf.cell(30, 10, price, 1, 0)
    pdf.cell(30, 10, total_price, 1, 1)


generate_date = datetime.now().strftime("%Y.%m.%d")
pdf = FPDF()
col_product_id = "Product ID"
col_product_name = "Product Name"
col_amount = "Amount"
col_price = "Price per Unit"
co_total_price = "Total Price"
title = "Invoice nr. 10001"
date = f"Date {generate_date}"
summary = f"The total due amount is {co_total_price} Euros"

# Draw a pdf
pdf.add_page()
pdf.set_font("Times", "B", 22)
pdf.cell(0, 10, title, 0, 1)
pdf.cell(0, 10, date, ln=1)
pdf.ln()
add_cell(col_product_id, col_product_name, col_amount, col_price, co_total_price)
pdf.output("./output/invoice.pdf")

