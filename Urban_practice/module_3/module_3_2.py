variants = ('.com', '.ru', '.net')

def send_email (message, recipient,*, sender  = "university.help@gmail.com"):
    if ('@' in recipient and '@' in sender) and (recipient.endswith(variants) and sender.endswith(variants)):
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
        else:
            if sender == "university.help@gmail.com":
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
            else:
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")



send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')