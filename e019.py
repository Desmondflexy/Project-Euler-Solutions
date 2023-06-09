"""
Problem 19 - Counting Sundays
"""

COUNTDAYS = 365
SUM = 0
for yy in range(1901, 2001):
    for mm in range(12):
        if mm == 1:
            if yy % 4 == 0 and yy % 100 != 0 or yy % 400 == 0:
                DAYS_OF_MONTH = 29
            else:
                DAYS_OF_MONTH = 28
        elif mm in [8, 3, 5, 10]:
            DAYS_OF_MONTH = 30
        else:
            DAYS_OF_MONTH = 31
        for dd in range(1, DAYS_OF_MONTH+1):
            COUNTDAYS += 1
            if COUNTDAYS % 7 == 0 and dd == 1:
                SUM += 1

print(SUM)


#===============================================
# from datetime import datetime
#
# count = 0
# for yy in range(1901, 2001):
#     for mm in range(1, 13):
#         if datetime(yy, mm, 1).weekday() == 6:
#             count += 1
# print(count)
#===============================================
