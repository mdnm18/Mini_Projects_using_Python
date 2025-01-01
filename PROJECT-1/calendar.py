import calendar
def display_calendar(year):
    print(calendar.TextCalendar().formatyear(year))

year = int(input("PLEASE ENTER A YEAR (e.g., 2006): "))
display_calendar(year)
