# -------- DAY 16 "Investment" --------
# Investing 100$ in a project whose annual profit is 10%,
# The program will print the total amount with the net profit after 7 years of investment.
# استثمار 100$ في مشروع ربحه السنوي 10% ,, سيقوم البرنامج بطباعة إجمالي المبلغ مع صافي الربح بعد 7 سنين من الاستثمار.


def invest(money, annual, years):
    profit = int((money + ((100 / annual) * years)))
    print('-'*21, f'\nThe Net Profit after {years} years is: {profit}$\nAnd the total amount is: {profit-100}$')


amount = int(input('Enter the amount you wish to invest: '))
percent = int(input('Enter the annual profit percentage: '))
year = int(input('Enter duration of the investment (in years): '))

invest(amount, percent, year)
