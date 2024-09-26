#first part
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(b=25)
print_params(c=[1,2,3])

#second part
values_list = [70, False, 'watermelon']
values_dict = {'a': 2, 'b': 'melon', 'c': 3.198}

print_params(*values_list)
print_params(**values_dict)

#third part
values_list_2  = [2.901, False]
print_params(*values_list_2, 42)

