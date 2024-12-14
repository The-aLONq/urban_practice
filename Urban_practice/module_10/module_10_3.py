import threading
import random
import time


class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(1,101):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            sum = random.randint(50,500)
            self.balance += sum

            print(f"Пополнение: {sum}. Баланс: {self.balance}")

            time.sleep(0.001)

    def take(self):
        for i in range(1,101):
            sum = random.randint(50,500)
            print(f'Запрос на {sum}')
            if sum <= self.balance:
                self.balance -= sum
                print(f"Снятие: {sum}. Баланс: {self.balance}")
            elif sum > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

            time.sleep(0.001)

bk = Bank(balance=0)

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')