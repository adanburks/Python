def is_leap_year(year):
    if year % 4 == 0:  # possible leap year
        if year % 100 == 0:  # possible leap year if also divisible by 400
            if year % 400 == 0: # leap year if divisible by all
                return True
            else:
                return False
        return True
    else:
        return False
