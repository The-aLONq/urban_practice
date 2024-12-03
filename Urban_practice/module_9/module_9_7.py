def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        return 'Простое чилосо' f'\n{num}' if count == 2 else 'Составное число' f'\n{num}'
    return wrapper

@is_prime
def sum_three(*args):
    if len(args) == 3:
        return sum(args)
    else:
        print('Программа расчитана на 3 числа')

result = sum_three(2,2,3)
print(result)