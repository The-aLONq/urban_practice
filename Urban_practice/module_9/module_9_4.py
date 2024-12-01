from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda string_pair: string_pair[0] == string_pair[1], zip(first, second)))

print(result)

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for index, string in enumerate(data_set, start=1):
                file.write(str(string) + '\n')

    return write_everything

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self, *args, **kwargs):
        return choice(self.words)


gt = get_advanced_writer('text.txt')
data_to_write = ['Привет', 'Как дела']

list(map(gt, data_to_write))

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())