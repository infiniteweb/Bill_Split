class Flatmate:
    """
    Object that creates each flatmate
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return round(to_pay)

class Bill:
    """
    Object that contains the receipt for the amount owed and the period that it's for.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period