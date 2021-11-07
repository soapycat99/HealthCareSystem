class Receipt():
    def __init__(self, amount: float, name: str, invoiceID: str = None):
        self.amount = amount
        self.name = name

    def getReceipt(self):
        return self.amount, self.name