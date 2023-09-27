import datetime
import random


def my_decorator(a_func):
    def wraper():
        now = datetime.datetime.now()
        print(now)
        a_func()
        now_1 = datetime.datetime.now()
        print(now_1)
        print(now_1 - now)

    return wraper


@my_decorator
def some_func():
    random_list = [random.randint(0, 20) for i in range(1000)]
    print(random_list)


@my_decorator
def some_func_2():
    random_list_2 = [random.randint(0, 20) for i in range(12000)]
    print(random_list_2)


some_func()
print('-' * 50)
some_func_2()
