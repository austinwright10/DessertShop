'''template for the receipt'''
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

def make_receipt(data, out_file_name):
    '''data which we are going to display as tables'''
    table_data = [["Name", "Quantity", "Unit Price", "Cost", "Tax"]]
    table_data.extend(data)
    # creating a Base Document Template of page size A4
    pdf = SimpleDocTemplate(out_file_name, pagesize=A4)

    # standard stylesheet defined within reportlab itself
    styles = getSampleStyleSheet()

    # fetching the style of the Top level heading (Heading1)
    title_style = styles["Heading1"]

    # 0: left, 1: center, 2: right
    title_style.alignment = 1

    # creating the paragraph with
    # the heading text and passing the styles to it
    title = Paragraph("Dessert Shop Receipt", title_style)

    # creates a Table Style object and in it,
    # defines the styles row-wise
    # the tuples which look like coordinates
    # are nothing but rows and columns
    style = TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (8, 6), 1, colors.black),
            ("BACKGROUND", (0, 0), (4, 0), colors.gray),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ]
    )
    # creates a table object and passes the style to it
    table = Table(table_data, style=style)

    # final step which builds the
    # actual PDF putting together all the elements
    pdf.build([title, table])

def main():
    '''Example data for the receipt'''
    data = [
        ["16/11/2020", "Full Stack Development with React & Node JS - Live",
        "Lifetime", "10,999.00/-"],
        ["16/11/2020", "Geeks Classes: Live Session", "6 months", "9,999.00/-"],
    ]

    make_receipt(data, "receipt.pdf")

if __name__ == "__main__":
    main()
