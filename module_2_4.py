numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
x=0
end=len(numbers)

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

for x in range(1,end):
    is_prime(numbers[x])
    if is_prime(numbers[x]):
        primes.append(numbers[x])
    if not is_prime(numbers[x]):
        not_primes.append(numbers[x])

print(primes)
print(not_primes)
