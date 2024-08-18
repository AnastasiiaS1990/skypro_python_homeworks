def is_year_leap(year):
    #if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    if (year % 4 == 0):
        return True
    else:
        return False
year = int(input())
print("Год", year, end=': ')
print(is_year_leap(year))