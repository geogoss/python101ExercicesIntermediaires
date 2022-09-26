
from datetime import date

def nombre_deJours(date1, date2):
    return (date2 - date1).days


date1 = date(2014, 7, 2)
date2 = date(2018, 7, 11)

print(nombre_deJours(date1, date2), "days")

# autre solution :

f_date = date(2014, 7, 2)
l_date = date(2018, 7, 11)

delta = l_date - f_date

print(delta.days)


