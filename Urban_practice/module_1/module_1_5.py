immutable_var = ("арбуз", 26, True, 4.04)
print(immutable_var)
#immutable_var[0] = "ананас" #кортеж неизменяемый, можно в него закинуть спискок и тогда получиться
print(immutable_var)

mutable_list = [1,2,3,4,5, "pomidorka"]
#print(mutable_list)
mutable_list[2] = "orange"
print(mutable_list)