# Here simple code which will check whether a year is leap year or not.
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """Takes a year and month and returns the number of days
    of the selected month."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "INVALID!"
    else:
        if is_leap(year) == True:
            if month_days[month - 1] == 28:
                return f"{month_days[month - 1] + 1}"
        return f"{month_days[month - 1]}"


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)