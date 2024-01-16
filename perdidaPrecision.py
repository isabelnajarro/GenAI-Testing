from decimal import Decimal, getcontext

getcontext().prec = 20

entero = Decimal('1000000000')
double = Decimal('0.0000000001')

res = entero + double
print(res)