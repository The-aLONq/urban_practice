import threading
import random
import time
from queue import Queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        random_time = random.randint(3,10)
        time.sleep(random_time)

    def __str__(self):
        return self.name

class Cafe:
    def __init__(self, tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f"{guest} сел(-а) за стол номер {table.number}")
                    break
            else:
                self.queue.put(guest)
                print(f'{guest} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()