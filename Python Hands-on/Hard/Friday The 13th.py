'''Given the month and year as numbers, return whether that month contains a Friday 13th.

Examples
has_friday_13(3, 2020) ➞ True

has_friday_13(10, 2017) ➞ True

has_friday_13(1, 1985) ➞ False'''



import datetime
from datetime import datetime
import calendar

def has_friday_13(month, year):
    date = '{} 13 {}'.format(month,year)
    day_num = datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[day_num]) == "Friday"


has_friday_13(3, 2020)
