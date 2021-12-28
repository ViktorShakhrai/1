# Создайте класс Soda (для определения типа газированной воды),
# принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}»
# в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».

class Soda:
    def __init__(self, dobavka=""):
        if isinstance(dobavka, str):
            self.dabavka = dobavka
        else:
            self.dabavka = None

    def show_my_drink(self):
        if self.dabavka:
            print("Газировка и {}".format(self.dabavka))
        else:
            print("Обычная газировка")


my_g = Soda("d")
my_g.show_my_drink()
