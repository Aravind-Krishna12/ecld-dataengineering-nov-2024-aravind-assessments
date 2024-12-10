#Reverse the date and save into a string format


def format_date(date):
       date_str = date.split('/')
       return f"{date_str[2]}{date_str[1]}{date_str[0]}"