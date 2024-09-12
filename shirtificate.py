from fpdf import FPDF

# Get name
name = input("Name: ")

# Create object
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=False, margin=0)

# Header
pdf.set_font("helvetica", "B", 30)
pdf.cell(w=0, h=30, text="CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

# Add image
pdf.image("shirtificate.png", x="C", y=70, w=180)

# Add text on image
pdf.set_text_color(255,255,255)
pdf.set_font("helvetica", size=20)
pdf.cell(w=0, h=150, text=f"{name} Harvard took CS50", align="C")

pdf.output("shirtificate.pdf")
