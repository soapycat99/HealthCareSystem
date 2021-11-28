import time
from datetime import date

STREET = '1003 US-231'
CITY = 'Troy, AL 36081'
PHONE = '334-670-5000'

class Receipt():
    def __init__(self, amount: str, des: str, invoiceID: str = None):
        self.amount = amount
        self.des = des

    @classmethod
    def get_time(self):
        t = time.localtime()
        current_time = time.strftime('%I:%M:%S%p', t)

        today = date.today()
        today = today.strftime('%m/%d/%y')

        return current_time, today

    def getReceipt(self):
        title = 'HeatlhCare System'

        length = len('-' * 10 + 'HealthCare System' + '-' * 10)


        content ='-' * 10 + 'HealthCare System' + '-' * 10 + '\n'

        content = content + '|' + ' ' * (18 + len(title)) + '|\n'

        content = content + '|' + STREET.center(length - 2) + '|\n' +\
                  '|' + CITY.center(length - 2) + '|\n' + \
                  '|' + PHONE.center(length - 2) + '|\n' + \
                  '| ' + '-' * (length - 4) + ' |\n'


        current_time, today = self.get_time()

        content = content + f'| {today:>20} {current_time:>12} |\n'

        content = content + '| ' + '-' * (length - 4) + ' |\n'

        amount = self.amount
        des = self.des

        length0 = length - len(des) - len(amount) - 3

        content = content + f'|  {des} {amount:>{length0}} |\n'

        return content,current_time,today

