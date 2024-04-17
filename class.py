class Phone:
    brand = 'Apple'
    model = 'iPhone 15 Pro Max'

    def display_info(self):
        print(f"Телефон: {self.brand}, Модель: {self.model}")

# Создание объекта класса Phone
my_phone = Phone()

# Вывод информации о телефоне
print(f"Бренд: {my_phone.brand}")
print(f"Модель: {my_phone.model}")
my_phone.display_info()


class Smartphone(Phone):
    def __init__(self, brand, model, operating_system):
        
        super().__init__()
      
        self.brand = brand
        self.model = model
        self.operating_system = operating_system

    def show_os_info(self):
        print(f"Операционная система: {self.operating_system}")


my_smartphone = Smartphone(brand='Samsung', model='Galaxy S21', operating_system='Android')

print(f"Бренд: {my_smartphone.brand}")
print(f"Модель: {my_smartphone.model}")
my_smartphone.display_info()
my_smartphone.show_os_info()
