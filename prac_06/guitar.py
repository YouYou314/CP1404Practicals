CURRENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} {self.year}: ${self.cost:,.2f}"

    def get_age(self):
        return