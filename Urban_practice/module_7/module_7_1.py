from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt' #необходимо заранее создать файл products.txt

    def get_products(self):
        file_open = open(self.__file_name, 'r')
        file_content = file_open.read()
        file_open.close()
        return file_content

    def add(self, *products):
        file_open = open(self.__file_name, 'r')
        file_content = file_open.read()
        file_open.close()

        for product in products:
            if product.name in file_content:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file_open = open(self.__file_name, 'a')
                file_open.write(str(product) + '\n')
                file_open.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
