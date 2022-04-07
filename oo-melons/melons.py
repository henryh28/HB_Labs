"""Classes for melon orders."""

from random import uniform
from datetime import datetime

class AbstractMelonOrder:
    """ An abstract base class that other Melon Orders inherit from """

    def __init__(self, species, qty):
        """ Initialize parent class attributes for orders """

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = ""
        self.tax = 0.0

        if self.qty > 100:
            raise TooManyMelonsError

    def get_total(self):
        """ Calculate price, including tax """
        base_price = self.get_base_price()
        gouge_rate, small_order_penalty = 1.5, 3
    
        if self.species == "Christmas":
            base_price *= gouge_rate

        total = (1 + self.tax) * self.qty * base_price

        if (self.__class__.__name__ == "InternationalMelonOrder"):
            if self.qty < 10:
                total += small_order_penalty

        return round(total,2)


    def mark_shipped(self):
        """ Record the fact than an order has been shipped """

        self.shipped = True


    def get_base_price(self):
        """ Implements 'splurge pricing' for base price  :( """ 

        rush_hour_charge = 0
        rush_hour_penalty = 4
        now = datetime.now()

        # check if current time is in rush hour window
        rush_hour_days = [1,2,3,4,5]
        rush_hour_hours = [8,9,10,11,12]

        if datetime.today().isoweekday() in rush_hour_days:
            if now.hour in rush_hour_hours:
                rush_hour_charge = rush_hour_penalty


        return (uniform(5,9)+ rush_hour_charge)

class DomesticMelonOrder(AbstractMelonOrder):
    """ A melon order within the USA """

    def __init__(self, species, qty):
        """ Initialize melon order attributes """

        super().__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """ An international (non-US) melon order """

    def __init__(self, species, qty, country_code):
        """ Initialize melon order attributes """

        super().__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """ Return the country code """

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """ A melon order for the government """

    def __init__(self, species, qty):
        """ Initialize government order attributes """
        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """ Marks whether or not a melon has passed inspection """
        self.passed_inspection = passed

class TooManyMelonsError(ValueError):
    """ Customm error to guard against orders that are too large """

    # reference: https://www.programiz.com/python-programming/user-defined-exception

    def __str__(self):
        return (f"No more than 100 melons!")




