numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
x=0
end=len(numbers)
for x in range(1,end):
    if numbers[x] % 2 == 0:
        if numbers[x] == 2:
            primes.append(numbers[x])
        else:
            not_primes.append(numbers[x])
    elif numbers[x] % 3 == 0:
        if numbers[x] == 3:
            primes.append(numbers[x])
        else:
            not_primes.append(numbers[x])
    else:
        primes.append(numbers[x])
print(primes)
print(not_primes)