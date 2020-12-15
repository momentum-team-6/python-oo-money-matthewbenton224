# pylint: disable=unidiomatic-typecheck,unnecessary-pass


class DifferentCurrencyError(Exception):
    pass


class Currency:
    """
    Represents a currency. Does not contain any exchange rate info.
    """

    def __init__(self, name, code, symbol=None, digits=2):
        self.name = name
        self.code = code
        self.symbol = symbol
        self.digits = digits

        """
        Parameters:
        - name -- the English name of the currency
        - code -- the ISO 4217 three-letter code for the currency
        - symbol - optional symbol used to designate currency
        - digits -- number of significant digits used
        """
        

    def __str__(self):
        return f"{self.symbol}{self.digits}"

        """
        Should return the currency code, or code with symbol in parentheses.
        """
        

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.name == other.name and
                self.code == other.code and self.symbol == other.symbol and
                self.digits == other.digits)


class Money:
    """
    Represents an amount of money. Requires an amount and a currency.
    """

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

        """
        Parameters:
        - amount -- quantity of currency
        - currency -- type of currency
        """
        
    def __str__(self):
        formated_amount = "{:.{}f}".format(self.amount, self.currency.digits)
        if self.currency.symbol:
            return f"{self.currency.symbol}{formated_amount}"
        else:
            return f"{self.currency.code} {formated_amount}"
        
        """
        Should use the currency symbol if available, else use the code.
        Use the currency digits to determine number of digits to show.
        """
        

    def __repr__(self):
        return f"<Money {str(self)}>"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """

        return (type(self) == type(other) and self.amount == other.amount and
                self.currency == other.currency)

    def add(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else: 
            raise DifferentCurrencyError

        """
        Add two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        

    def sub(self, other):
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        else:
            raise DifferentCurrencyError
        """
        Subtract two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        

    def mul(self, multiplier):
        """
        Multiply a money object by a number to get a new money object.
        """
        return Money(self.amount * multiplier, self.currency)

    def div(self, divisor):
        """
        Divide a money object by a number to get a new money object.
        """
        return Money(self.amount / divisor, self.currency)
