# -------- DAY 17 "Leap Year" --------
# NOTE: NOT exactly understood!


def check_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f'{year} is a LEAP year.')
    else:
        print(f'{year} is NOT a leap year.')


year = int(input('Enter a year: '))
check_year(year)
