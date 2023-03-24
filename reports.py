from fpdf import FPDF


class PdfReport:
    """
    Object that generates a PDF report based on inputs of the other objects
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()
        pdf.set_font(family="Times", size=24, style="B")
        pdf.image(name="/Users/nathantye/PycharmProjects/bill_split_app/Images/house.png", w=60, h=60)
        pdf.cell(w=0, h=80, txt="Flatmates Bill", align="C", ln=1)
        pdf.cell(w=100, h=40, txt="Period: ")
        pdf.cell(w=0, h=40, txt=f"{bill.period}", ln=1)
        pdf.cell(w=100, h=40, txt=f"{flatmate1.name}")
        pdf.cell(w=100, h=40, txt=f"{flatmate1.pays(bill=bill, flatmate2=flatmate2)}", ln=1)
        pdf.cell(w=100, h=40, txt=f"{flatmate2.name}")
        pdf.cell(w=100, h=40, txt=f"{flatmate2.pays(bill=bill, flatmate2=flatmate1)}")
        pdf.output(self.filename)
