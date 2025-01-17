class Vechile:
    __model = 'Toyota'
    __engine_power = 200
    __color = 'white'
    __COLOR_VARIANTS = ['orange', 'purple', 'black', 'chrome']
    def __init__(self, owner):
        self.owner = owner

    def get_model(self):
        return (f'Модель:{self.__model}')

    def get_horsepower(self):
        return (f'Мощность двигателя:{self.__engine_power}')

    def get_color(self):
        return (f'Цвет:{self.__color}')

    def print_info(self):
        print(f' {self.get_model()}\n {self.get_horsepower()}\n {self.get_color()}\n Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f' Нельзя сменить цвет на {new_color}')




class Sedan(Vechile):
    __PASSANGERS_LIMIT = 5
    def __init__(self, owner):
        super().__init__(owner)


vehicle1 = Sedan('Dendi')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()


