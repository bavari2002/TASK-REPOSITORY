# date = int(input("please enter the date (1-31): "))
# month = int(input("please enter the months (1-12): "))
# year = int(input("please enter the year: "))

# print(f"You enter : Date {date}, Month {month}, Year {year}")

# year = int((input("please enter the year (YYYY):     ")))

# if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"Year {year} is Kabisat")
# else:
#     print(f"Year {year} is not Kabisat")

# date = int(input("enter date (1-31): "))
# month = int(input("enter month (1-12): "))

# if date < 1 or date > 31 or month < 1 or month > 12:
#     print("date or month not valid")
# else:
#     print("date or onth valid")


def is_kabisat(year):
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def numberof_day_in_month(month, year):
    if month == 2:
        return 29 if is_kabisat(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def enter_number(message, min_val=None, max_val=None):
    while True:
        try:
            number = int(input(message))
            if min_val is not None and number < min_val:
                print(f"Minimal Value {min_val}.")
            elif max_val is not None and number > max_val:
                print(f"Maximal Value {max_val}.")
            else:
                return number
        except ValueError:
            print("You must enter in the form of numbers.")


def validate_input():
    date = enter_number("Enter date (1-31): ", 1, 31)
    month = enter_number("Enter month (1-12): ", 1, 12)
    year = enter_number("Enter year (positive): ", 1)

    max_day = numberof_day_in_month(month, year)
    while date > max_day:
        print(f"Invalid date! Month {month} year {year} only until {max_day}.")
        date = enter_number(f"Enter date (1-{max_day}): ", 1, max_day)
    return date, month, year


def zeller_congruence(date, month, year):
    if month < 3:
        month += 12
        year -= 1

    k = year % 100
    m = month
    j = year // 100
    h = (date + (13 * (m + 1)) // 5 + k + (k // 4) + (j // 4) - (2 * j)) % 7

    day = {
        0: "Saturday",
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday"
    }
    return day[h]


date, month, year = validate_input()
day = zeller_congruence(date, month, year)
print(f"The date {date}/{month}/{year} is {day}.")
