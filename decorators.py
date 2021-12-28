# def my_shiny_new_decorator(function_to_decorate):
#     # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
#     # получая возможность исполнять произвольный код до и после неё.
#     def the_wrapper_around_the_original_function():
#         print("Я - код, который отработает до вызова функции")
#         function_to_decorate()  # Cама функция
#         print("А я - код, срабатывающий после")
#         # Вернём эту функцию
#
#     return the_wrapper_around_the_original_function
#
#
# # Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
# def alone_func():
#     print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")
#
#
# # Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
# # который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
# # готовую к использованию функцию:
# alone_func = my_shiny_new_decorator(alone_func)
# alone_func()
#
#
# @my_shiny_new_decorator
# def another_alone_function():
#     print("Я інша одинока функція")
#
#
# another_alone_function()


def bread(func):
    def wrapper():
        print("Верхня булка")
        func()
        print("Нижня булка")

    return wrapper


def ingradients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")

    return wrapper


@bread
@ingradients
def sandwich(food="--ветчина--"):
    print(food)


sandwich()


# Передача декоратором аргументов в функцию
def a_decorator_passing_arguments(function_to_decorate):
    def wrapper_accepting_arguments(arg, arg2):
        print("Look what i got:", arg, arg2)
        function_to_decorate(arg, arg2)

    return wrapper_accepting_arguments


# Теперь, когда мы вызываем функцию, которую возвращает декоратор, мы вызываем её "обёртку",
# передаём ей аргументы и уже в свою очередь она передаёт их декорируемой функции
@a_decorator_passing_arguments
def full_name(name, surname):
    print("My name:", name, surname)


full_name("Viktor", "Shakhrai")

#Декорирование методов
def method_frendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie -= 3
        return method_to_decorate(self, lie)

    return wrapper

class Lucy:
    def __init__(self):
        self.age = 32
    @method_frendly_decorator
    def sey_your_age(self,lie):
        print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))

l = Lucy()
l.sey_your_age(-3)