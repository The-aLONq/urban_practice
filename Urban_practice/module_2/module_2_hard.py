def password_generade(number_user):
    result = ""

    for i in range(1,21):
        for j in range(1+i,21):
            sum = i + j
            if number_user % sum == 0:
                result += f'{i}{j}'
    return result

number_user = int(input("Введите любое число от 3 до 20 включительно: "))

if number_user < 3 or number_user > 20:  # проверка на валидность
    print("Ведите число согласно правилам.")
else:
    password = password_generade(number_user)
    print(f"Пароль для чила {number_user}: {password}")


