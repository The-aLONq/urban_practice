my_dict = {'Red': 1, 'White': 2, 'Purple': 3}
print(my_dict)
print(my_dict.get('White'))
print(my_dict.get('Blue', "Привет, такого ключа в словаре нет("))
my_dict.update({'Black': 9, 'Orange': 7})
print(my_dict)
a = my_dict.pop('White')
print(a)
print(my_dict)

my_set = {1,1,1,2,2,3,4,5, False, False, 'red'}
print(my_set)
my_set.add(8)
my_set.add('banana')
print(my_set)
my_set.discard(1)
print(my_set)