def personal_sum(*numbers):
    result = 0
    incorrect_data = 0
    has_incorrect_data = False

    for number in numbers:
        try:
            result += number
        except TypeError:
            if not has_incorrect_data:
                print('В numbers записан некорректный тип данных')
                has_incorrect_data = True
            incorrect_data  += 1
    return result,incorrect_data

def calculate_average(numbers):
    try:
        total, incorrect_data = personal_sum(*numbers)
    except TypeError:
        return None

    count  = len(numbers) - incorrect_data
    try:
        avg = total / count
        return avg
    except ZeroDivisionError:
        return 0
    except TypeError:
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать