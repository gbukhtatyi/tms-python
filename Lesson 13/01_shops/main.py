import shops

# Test CoffeShop

coffe_shop = shops.CafeShop()
pizza = shops.Pizza(1, "Пицца", 100, ['Пеперони', 'Сыр'], False, 30)
cofee100 = shops.Coffee(2, "Кофе 100ml", 10, 100)

for product in pizza, cofee100:
    coffe_shop.add_product(product)
coffe_shop.add_product(cofee100)
coffe_shop.add_product(cofee100)

print('Test CoffeShop')
print(coffe_shop.all_products())
print(coffe_shop.sells)

# Test FurnitureShop

furniture_shop = shops.FurnitureShop()

table = shops.Table(1, "Стол", 2000)
chair = shops.Chair(2, "Стул", 1000)
cupboard = shops.Cupboard(3, "Шкаф", 3000)

for product in table, chair, cupboard:
    furniture_shop.add_product(product)

furniture_shop.sell_product(chair)
furniture_shop.sell_product(chair)
furniture_shop.sell_product(table)

print('Test FurnitureShop')

print(furniture_shop.all_products())
print(furniture_shop.sells)

# Test BookShop

book_shop = shops.BookShop()

book = shops.Book(1, "Книга", 2000)
journal = shops.Journal(2, "Журнал", 1000)

for product in book, journal:
    book_shop.add_product(product)

print('Test BookShop')

print(book_shop.all_products())
print(book_shop.sells)

# Test PcShop
pc_shop = shops.PcShop()

memory_1gb = shops.Memory(1, "1 gb", 2000)
memory_2gb = shops.Memory(2, "2 gb", 4000)

for product in memory_1gb, memory_2gb:
    pc_shop.add_product(product)

print('Test PcShop')
print(pc_shop.all_products())
print(pc_shop.sells)
