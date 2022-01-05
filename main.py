from datetime import datetime
import os


def my_decorator(old_function):
    def new_function(*args, **kwargs):
        start = datetime.now()
        result = old_function(*args, **kwargs)
        function_name = old_function.__name__
        file_path = os.path.abspath('info_function.log')
        with open('info_function.log', 'a+', encoding='utf-8') as file:
            file.write(f'\nИмя функции: {function_name} \nВремя начала: {start} \nАргументы: {args},{kwargs}'
                        f'\nРезультат: {result} \nПуть: {file_path}')
        return result
    return new_function



@my_decorator
def my_func(*args, **kwargs):
    result = 'Функция запущена!'
    return result


res = my_func(3, 12, 72, info1=90, info2=5)
print(res)



nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None]
]

@my_decorator
def generator_nested_list(nested_list):
    for value in nested_list:
        if isinstance(value, list):
            for item in value:
                yield item
        else:
            yield value


for item in generator_nested_list(nested_list):
    print(item)