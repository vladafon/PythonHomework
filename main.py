from LibaDZ import functions as f

@f.type_check(a=int,pow=int)
@f.cache_decorator
def power(a, pow=2):
    return a**pow

print(power(3, 9))
print(power(2, 4))
print(power(2, 5))
print(power(2, 4))
print(power(3, 9))
print(power(3,2))
print(power(3,))

#print(power(3,'3'))

print(power('3',4))
