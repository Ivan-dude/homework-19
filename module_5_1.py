class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if new_floor <= self.number_of_floors and new_floor > 0:
                print(i, 'этаж')
            else:
                print('Такого этажа не существует')
                break
h1 = House('ЖК "Горский"', 30)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)