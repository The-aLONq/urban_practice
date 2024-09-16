phone_book = {'Denis': 88005553535, 'Max': 8800553534}
phone_book['Denis'] = 123124124
phone_book['Denis2222'] = 123124124123123
del phone_book['Denis2222']
phone_book.update({'Sasha': 111111111111,
                  'Banana': 123123123123}) #добавляет к товему словарю
print(phone_book.get('Denis1', 'такого ключа нету')) #ищет по ключу
print(phone_book)
a = phone_book.pop('Max')
print(phone_book)


set_ = {1,2,3,4,5,6,1,2,5,6,2,9}
list = [1,2,2,2,2,2,1,1,1,14]
list = set(list)
print(list)
print(list.add(5))
print(list)
