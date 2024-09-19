class House:
    def __init__(self, name: str, number_of_floors: int):
        """Инициализатор класса"""
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        """Метод класса"""
        if 1 <= new_floor <= self.number_of_floors:
            for n in range(new_floor):
                print(n + 1)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        """Позволяет применять функцию len() к экземплярам класса"""
        return self.number_of_floors

    def __str__(self):
        """Применяется для отображения информации об объекте класса для пользователей,
        например для функций print, str."""
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


# Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# # __str__
print(h1)
print(h2)

# # __len__
print(len(h1))
print(len(h2))
