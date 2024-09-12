from fpdf import FPDF

class Shirtificate(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self.set_auto_page_break(auto=False, margin=0)

    def header(self):
        # Add title "CS50 Shirtificate" centered at the top
        self.set_font("Helvetica", "B", size=24)
        self.cell(w=0, h=30, text="CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")


    def add_shirt_image(self):
        # Add shirtificate.png image
        self.image("shirtificate.png", x="C", y=70, w=180)

    def add_name(self, name):
        # Add the user's name in white text on top of the shirt
        self.set_text_color(255,255,255)
        self.set_font("helvetica", size=20)
        self.cell(w=0, h=150, text=f"{name} Harvard took CS50", align="C")


def main():
    name = input("Name: ")

    # Create PDF
    pdf = Shirtificate()
    pdf.header()
    pdf.add_shirt_image()
    pdf.add_name(name)

    # Save the PDF
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
