from calendar import monthrange
from reports import PdfReport
from flat import Flatmate, Bill


months = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}

while True:
    try:
        bill_amount = input("Hey user, enter the bill amount: ")
        bill_amount = int(bill_amount)
        break
    except ValueError:
        print("I'm sorry please enter a valid input.")

while True:
    try:
        bill_input = input("What is the bill period? E.g. December 2020: ")
        bill_string = bill_input.split()
        bill_month_key = bill_string[0].title()
        bill_month = months[bill_month_key]
        bill_year = bill_string[1]
        bill_year = int(bill_year)
        bill_date = f"{bill_month} / {bill_year}"
        break
    except (KeyError, ValueError):
        print("Im sorry,please enter a valid date ")

while True:
    try:
        flatmate1_name = input("What is your name? ")
        flatmate1_name = str(flatmate1_name)
        break
    except ValueError:
        print("Im sorry, please enter a valid name. ")

while True:
    try:
        flatmate1_stay = input(f"How many days did {flatmate1_name} stay in the house during the bill period? ")
        flatmate1_stay = int(flatmate1_stay)
        input_check = monthrange(bill_year, bill_month)
        max_days = input_check[1]
        if max_days >= flatmate1_stay >= 0:
            break
        else:
            print(f"Error: {flatmate1_name} must of stayed between 0 and {max_days} days during the bill period.")
    except ValueError:
        print("Im sorry, please enter a number. ")

while True:
    try:
        flatmate2_name = input("What is the name of the other flatmate? ")
        flatmate2_name = str(flatmate2_name)
        break
    except ValueError:
        print("Im sorry, please enter a valid name. ")

while True:
    try:
        flatmate2_stay = input(f"How many days did {flatmate2_name} stay in the house during the period? ")
        flatmate2_stay = int(flatmate2_stay)
        input_check = monthrange(bill_year, bill_month)
        max_days = input_check[1]
        if max_days >= flatmate2_stay >= 0:
            break
        else:
            print(f"Error: {flatmate2_name} must of stayed between 0 and {max_days} days during the bill period.")
        break
    except ValueError:
        print("Im sorry, please enter a number. ")

flatmate1 = Flatmate(name=flatmate1_name, days_in_house=flatmate1_stay)

flatmate2 = Flatmate(name=flatmate2_name, days_in_house=flatmate2_stay)

the_months_bill = Bill(bill_amount, bill_date)

# john = Flatmate(name="John", days_in_house=30)
# chloe = Flatmate(name="Chloe", days_in_house=25)
# the_months_bill = Bill(amount=1000, period="12/2020")

# print(f"{flatmate1.name} pays: ", flatmate1.pays(bill=the_months_bill, flatmate2=flatmate2))
# print(f"{flatmate2.name} pays: ", flatmate2.pays(bill=the_months_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_months_bill)
