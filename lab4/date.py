from datetime import datetime, timedelta

#TASK 1
"""
current_date = datetime.now()
new_date = current_date - timedelta(days = 5)
print(new_date)
"""

#TASK 2
"""
today = datetime.now()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)
print(yesterday, today, tomorrow, sep = "\n")
"""

#TASK 3
"""
current_date = datetime.now()
date_without_microseconds = current_date.replace(microsecond=0)
print(date_without_microseconds)
"""

#TASK 4
"""
date1 = datetime(2024, 2, 1, 12, 0, 0)
date2 = datetime.now()

difference = abs((date2 - date1).total_seconds())
print(difference)
"""