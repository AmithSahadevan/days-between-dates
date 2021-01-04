from datetime import date

first_date = date(2021,1,1)
last_date = date(2021,1,10)

result = last_date-first_date
print(result.days)