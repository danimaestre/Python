###  Dates  ####

from datetime import datetime

now = datetime.now()


timestamp = now.timestamp()


year_2023 = datetime(2023, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
    
print_date(now)
print_date(year_2023)

from datetime import time

current_time = time(21, 6, 45)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


from datetime import date

current_date = date.today() # Genera objeto vacio
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2023, 5, 23) # Hay que pasarle valores
print(current_date)

print(current_date.year)
print(current_date.month)
print(current_date.day)

# Operaciones con fechas

current_date = date(current_date.year + 10, current_date.month + 3, current_date.day + 8)
print(current_date)

''' Modulo para operar con fechas '''

diff = now - year_2023
print(diff)
diff = current_date - year_2023.date()
print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)


print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
print(end_timedelta / start_timedelta)


