from datetime import datetime


def my_decorator(old_function):
    def new_function(*args, **kwargs):
        start = datetime.now()
        result = old_function(*args, **kwargs)
        function_name = old_function.__name__
        with open('info_function.log', 'a+', encoding='utf-8') as file:
            file.write(f'\nИмя функции: {function_name} \nВремя начала: {start} \nАргументы: {args},{kwargs}'
                        f'\nРезультат: {result}')
        return result
    return new_function



@my_decorator
def my_func(*args, **kwargs):
    result = 'Функция запущена!'
    return result


res = my_func(3, 12, 72, info1=90, info2=5)
print(res)