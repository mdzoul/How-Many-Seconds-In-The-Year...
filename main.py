# Todo: Print totalDays, totalHours, totalMin as well

from replit import clear

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


def days_in_month(year):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        print(f"\n{year} is a leap year.")
        monthDays.remove(28)
        monthDays.append(29)
    else:
        print(f"\n{year} is not a leap year.")
    return monthDays


def calculate_seconds_in_year(monthDays):
    totalDays = sum(monthDays)
    totalHours = totalDays * 24
    totalMin = totalHours * 60
    totalSec = totalMin * 60
    return totalSec


endYearCheck = False
while not endYearCheck:
    year = int(input("Enter a year: "))

    monthDays = days_in_month(year)
    totalSec = calculate_seconds_in_year(monthDays)
    print(f"There are {totalSec:,} seconds in the year {year}.")

    if input(
            "\nWould you like to calculate another year? Y/N ").lower() == 'n':
        endYearCheck = True
    else:
        clear()
