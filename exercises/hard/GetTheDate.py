'''Write a function that, given a date (in the format MM/DD/YYYY), 
returns the day of the week as a string. 
Each day name must be one of the following strings: 
"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", or "Saturday".

To illustrate, the day of the week for "12/07/2016" is "Wednesday".

Examples
get_day("12/07/2016") ➞ "Wednesday"

get_day("09/04/2016") ➞ "Sunday"

get_day("12/08/2011") ➞ "Thursday"'''

from datetime import datetime
import calendar
def get_day(day):
    day_num = datetime.strptime(day, '%d/%m/%Y').weekday()
    return calendar.day_name[day_num]


day = input("Enter the date in dd/MM/yyyy format : ")
print(get_day(day))
	