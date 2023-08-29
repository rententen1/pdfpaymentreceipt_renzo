# imports module
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
#data which we are going to display as tables
DATA = [
    ["Date", "Name", "Subscription", "Price ($)"],
    [
        "8/28/2023"
        "Spotify Premium",
        "1 Month"
        "$4.99",
    ],
    [ "10/27/2023", "Chegg", "1 Month", "$9.99"],
    ["Subtotal", "", "$14.98"],
    ["Discount", "", "$-5.00"],
    ["Total", "", "$9.98"],
]

# creating a Base Document Template of page size A4
pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4)

#standard stylesheet defined within reportlab itself
styles = getSampleStyleSheet()

#fetching the style of Top Level heading (Heading1)
title_style = styles[ "Heading 1" ]

#0: left, 1: center, 2 : right
title_style.alignment = 1

# creating the paragraph with
# the heading text and passing the styles of it
title = Paragraph("GeeksforGeeks", title_style)

# creates a Table Style object and in it,
# defines the styles row wise
# the tuples which look like coordinates
# are nothing but rows and columns
style = TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (4, 4), 1, colors.black),
        ("BACKGROUND", (0, 0), (3, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.lavender),
    ]
)

# creates a table object and passes the style to it
table = Table(DATA, style=style)

# final step which builds the
# actual pdf putting together all the elements
pdf.build([title, table])
