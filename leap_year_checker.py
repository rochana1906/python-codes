def is_leap_year(year):
    # if divisible by 4
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


print(is_leap_year(2400))  # True
print(is_leap_year(1989))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(2100))  # False
