import datetime
x = datetime.datetime.now()
print(x)
print(type(x))
from datetime import date
date = date(2023, 4, 8)
print(date)
date = date.strftime("%Y-%m-%d")
print(type(date))
print(date) 
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

