
def prime_factorization_r(n, i, factors, result):
    if n == 0:
        result.append(factors[:])
        return
    if n < 2:
        return
    while i <= n:
        if is_prime(i):
            factors.append(i)
            prime_factorization_r(n - i, i, factors, result)
            factors.pop()
        i += 1

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i ==0:
            return False
    return True

result = []
prime_factorization_r(7, 2, [], result)
print(result)


print('                                   pauza             ')
def prime_factorization_i(n):
    prime_numbers = [x for x in range(2, n+1) if is_prime(x)]
    result = []
    stack = [(0, [], 0)]
    while stack:
        total, factors, start = stack.pop()
        if total == n:
            result.append(factors[:])
            continue
        for i in range(start, len(prime_numbers)):
            if total + prime_numbers[i] > n:
                break
            stack.append((total + prime_numbers[i], factors + [prime_numbers[i]], i))
    result.sort(key=lambda x: sorted(x))
    return result

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i ==0:
            return False
    return True

print(prime_factorization_i(7))
