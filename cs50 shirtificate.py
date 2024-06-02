from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font("Arial", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

    def footer(self):
        pass

    def shirt(self, name):
        # Set up page
        self.add_page("P", "A4")
        self.set_auto_page_break(auto=True, margin=15)
        
        # Draw shirt
        self.set_fill_color(255, 255, 255)
        self.rect(40, 100, 130, 180, "F")
        self.image("shirt.png", x=40, y=100, w=130)
        
        # Name
        self.set_text_color(255, 255, 255)
        self.set_font("Arial", "B", 16)
        self.text(105, 140, name, align="C")

def main():
    name = input("Enter your name: ")
    pdf = Shirtificate()
    pdf.shirt(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
