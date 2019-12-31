
MONTHS = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31,
          'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31,
          'November': 30, 'December': 31}


def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        if month == 2:
            if is_leap_year(year):
                return 29
            return 28
        return 28


def next_day(year, month, day):
    """
    Function to return the next calendar day.
    @param year:
    @param month:
    @param day:
    @return:
    """
    if day < days_in_month(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1


def is_leap_year(year):
    if year % 400 == 0 or year % 4 == 0:
        return True
    if year % 100 == 0:
        # not a leap year
        return False
    # if year % 4 == 0:
    #     return True
    return False
    # return True if year % 400 == 0 or year % 4 == 0


def date_is_before(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def days_between_dates(year1, month1, day1, year2, month2, day2):
    days = 0
    # assert not
    while date_is_before(year1, month1, day1, year2, month2, day2):
        year1, month1, day1, = next_day(year1, month1, day1)
        days += 1
    return days


if __name__ == '__main__':
    print(is_leap_year(2020))
    print(next_day(2013, 1, 1) == (2013, 1, 2))
    print('Tests passed!')