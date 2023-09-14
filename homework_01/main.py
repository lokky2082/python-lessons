"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    if args == None:
       return []
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num**2 for num in args]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"
def is_prime(num):
    if num == None:
        return False
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                return False
        return True
    else:
        return False

def filter_numbers(nums, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if(nums == None):
       return []
    if filter_type == ODD:
       return list(filter(lambda num: (num % 2) != 0, nums))
    if filter_type == EVEN:
       return list(filter(lambda num: (num % 2) == 0, nums))
    if filter_type == PRIME:
       return list(filter(is_prime, nums))
