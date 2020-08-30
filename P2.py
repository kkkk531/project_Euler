sum = 0
prvni = 1
druhe = 2

while druhe < 4000000:
    if druhe % 2 == 0:
        sum = sum + druhe
    print(druhe)
    druhe_2 = druhe
    druhe = prvni + druhe
    prvni = druhe_2

print('The sum of the even-valued terms of Fibonacci numbers below four million is:', sum)
