def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def count_days(d, m, y):
    month_days = [31, 28, 31, 30, 31, 30, 31,
                  31, 30, 31, 30, 31]
    
    total_days = y * 365 + d

    for i in range(m - 1):
        total_days += month_days[i]

    leap_years = y // 4 - y // 100 + y // 400
    if m <= 2:
        leap_years -= 1
    total_days += leap_years

    return total_days

date1 = (20, 4, 2025)
date2 = (25, 4, 2025)

days1 = count_days(*date1)
days2 = count_days(*date2)

print("Number of days between the two dates:", abs(days2 - days1))

# Output: 
# Number of days between the two dates: 5