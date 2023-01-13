def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def back_prime_nr_sum_r(n, i, factors, result):
    if n == 0:
        result.append(factors[:])
        return
    if n < 2:
        return
    while i <= n:
        if is_prime(i):
            factors.append(i)
            back_prime_nr_sum_r(n - i, i, factors, result)
            factors.pop()
        i += 1


def back_prime_nr_sum_i(n):
    prime_numbers = [x for x in range(2, n + 1) if is_prime(x)]
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


def start():
    while True:
        print('Descompunerea unui numar in suma de nr prime:')
        option = input('Selectati recursiv sau iterativ: ')
        option.lower().strip()
        if option == 'recursiv' or option == 'r':
            try:
                nr = int(input('Introduceti un nr intreg pozitiv: '))
                result = []
                back_prime_nr_sum_r(nr, 2, [], result)
                print('Rezolvare recursiva:')
                print(result)
            except ValueError:
                print('Valoarea introdusa nu este un ntreg pozitiv!')
        elif option == 'iterativ' or option == 'i':
            try:
                nr = int(input('Introduceti un nr intreg pozitiv: '))
                print('Rezolvare iterativa:')
                print(back_prime_nr_sum_i(nr))
            except ValueError:
                print('Valoarea introdusa nu este un ntreg pozitiv!')
        else:
            print('Optiune invalida!')


start()
