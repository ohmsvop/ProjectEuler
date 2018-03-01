# Counting Sundays
# from 1901-1-1 to 2000-12-31
from datetime import datetime
    
sunday = 0
for year in range(1901, 2001):
    for month in range(1,13):
        weekday = datetime(year, month, 1).weekday()
        if weekday == 6: # sunday = 6
            sunday += 1
print sunday
