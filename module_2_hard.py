import random
n=random.randint(3,20)
print(n)
result = []
for x in range(1,20):
    for y in range(1, 20):
        if x!=y:
            m=x+y
            if x < n and y < n:
                if (m % n) == 0 or (n % m) == 0:

                    result.append(x)
                    result.append(y)

                if (m % n) != 0 or (n % m) != 0:
                    continue
            else:
                continue
        else:
            continue
print(result)