def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'a', encoding='utf-8') as file_open:
        for index, string in enumerate(strings, start=1):
            position = file_open.tell()
            file_open.write(string + '\n')
            strings_positions[(index, position)] = string

    return strings_positions

result = custom_write('test.txt', [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
])

for elem in result.items():
    print(elem)