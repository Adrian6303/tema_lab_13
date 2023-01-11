def prime_factorization_r(n, i, factors):
    if n == 1:
        print(factors)
        return
    while i * i <= n:
        if n % i == 0:
            if is_prime(i):
                factors.append(i)
            prime_factorization_r(n // i, i, factors)
            factors.pop()
        i += 1
    if n > 1 and is_prime(n):
        factors.append(n)
        prime_factorization_r(1, i, factors)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i ==0:
            return False
    return True


def prime_factorization_i(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def start():
    while True:
        print('Descompunerea unui numar in suma de nr prime:')
        option = input('Selectati recursiv sau iterativ: ')
        option.lower().strip()
        if option =='recursiv':
            try:
                nr=int(input('Introduceti un nr intreg pozitiv: '))
                prime_factorization_r(nr, 2, [])
            except ValueError:
                print('Valoarea introdusa nu este un ntreg pozitiv!')
        elif option == 'iterativ':
            try:
                nr=int(input('Introduceti un nr intreg pozitiv: '))
                print(prime_factorization_i(nr))
            except ValueError:
                print('Valoarea introdusa nu este un ntreg pozitiv!')
        else:
            print('Optiune invalida!')

start()


