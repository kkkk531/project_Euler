sum = 0
i = 0

while i<1000:
    if i%3==0 or i%5==0:
        sum = sum+i
    i = i+1

print('The sum of the multiples of 3 and 5 below 1000 is:', sum)


