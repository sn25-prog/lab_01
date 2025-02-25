### Лабораторная работа № 1: Выражения и управляющие инструкции

# Вопрос 1. 
def _q_01():
    """
    Часть 1
    >>> 3                                                       # doctest: +SKIP
    ______
    >>> 2 + 3                                                   # doctest: +SKIP
    ______
    >>> -16 - -16                                               # doctest: +SKIP
    ______
    >>> 3 * 4 + 1                                               # doctest: +SKIP
    ______
    >>> 3 * (4 + 1)                                             # doctest: +SKIP
    ______
    >>> 2 ** 3                                                  # doctest: +SKIP
    ______
    
    Часть 2
    >>> x = 4                                                   # doctest: +SKIP
    >>> 3 + x                                                   # doctest: +SKIP
    ______
    >>> x + y                                                   # doctest: +SKIP
    ______
    >>> x, y = 1, 2                                             # doctest: +SKIP
    >>> 3 + x                                                   # doctest: +SKIP
    ______
    >>> x + y                                                   # doctest: +SKIP
    ______

    Часть 3
    >>> from operator import mul, add                           # doctest: +SKIP
    >>> mul(3, 4)                                               # doctest: +SKIP
    ______
    >>> mul(3, add(4, 1))                                       # doctest: +SKIP
    ______
    >>> pow(2, 3)                                               # doctest: +SKIP
    ______
    >>> pow(pow(2, 3), abs(-2))                                 # doctest: +SKIP
    ______
    """
    return 0

# Вопрос 2.
def _q_02():
    """
    Часть 1
    >>> def xk(c, d):                                           # doctest: +SKIP
    ...     if c == 4:
    ...         return 6
    ...     elif d >= 4:
    ...         return 6 + 7 + c
    ...     else:
    ...         return 25
    >>> xk(10, 10)                                              # doctest: +SKIP 
    ______
    >>> xk(10, 6)                                               # doctest: +SKIP
    ______
    >>> xk(4, 6)                                                # doctest: +SKIP
    ______
    >>> xk(0, 0)                                                # doctest: +SKIP
    ______

    Часть 2
    >>> def how_big(x):                                         # doctest: +SKIP
    ...     if x > 10:
    ...         print('очень много')
    ...     elif x > 5:
    ...         return 'много'
    ...     elif x > 0:
    ...         print('мало')
    ...     else:
    ...         print("нисколько")
    >>> how_big(7)                                              # doctest: +SKIP
    ______
    >>> how_big(12)                                             # doctest: +SKIP
    ______
    >>> how_big(1)                                              # doctest: +SKIP
    ______
    >>> how_big(-1)                                             # doctest: +SKIP
    ______

    Часть 3
    >>> n = 3                                                   # doctest: +SKIP
    >>> while n >= 0:                                           # doctest: +SKIP
    ...     n -= 1
    ...     print(n)
    ______

    Часть 4
    >>> positive = 28                                           # doctest: +SKIP
    >>> while positive:                                         # doctest: +SKIP
    ...    print("positive?")
    ...    positive -= 3
    ______

    Часть 5
    >>> positive = -9                                           # doctest: +SKIP
    >>> negative = -12                                          # doctest: +SKIP
    >>> while negative:                                         # doctest: +SKIP
    ...    if positive:
    ...        print(negative)
    ...    positive += 3
    ...    negative += 3
    ______
    """
    return 0

# Вопрос 3.
def _q_03():
    """
    Часть 1
    >>> True and 13                                             # doctest: +SKIP
    ______
    >>> False or 0                                              # doctest: +SKIP
    ______
    >>> not 10                                                  # doctest: +SKIP
    ______
    >>> not None                                                # doctest: +SKIP
    ______

    Часть 2
    >>> True and 1 / 0 and False                                # doctest: +SKIP
    ______
    >>> True or 1 / 0 or False                                  # doctest: +SKIP
    ______
    >>> True and 0                                              # doctest: +SKIP
    ______
    >>> False or 1                                              # doctest: +SKIP
    ______
    >>> 1 and 3 and 6 and 10 and 15                             # doctest: +SKIP
    ______
    >>> 0 or False or 2 or 1 / 0                                # doctest: +SKIP
    ______

    Часть 3
    >>> not 0                                                   # doctest: +SKIP
    ______
    >>> (1 + 1) and 1                                           # doctest: +SKIP
    ______
    >>> 1/0 or True                                             # doctest: +SKIP
    ______
    >>> (True or False) and False                               # doctest: +SKIP
    ______
    """
    return 0

# Вопрос 4.
def both_positive(x, y):
    """
    Возвращает True, если x и y — положительные.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x and y > 0                      # эту строчку можно и нужно изменить

# Вопрос 5.
def sum_digits(n):
    """
    Суммирует все цифры n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # проверяет применение return, а не print
    >>> x
    6
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 6.
def _q_06():
    """
    Часть 1
    >>> def ab(c, d):                                           # doctest: +SKIP
    ...     if c > 5:
    ...         print(c)
    ...     elif c > 7:
    ...         print(d)
    ...     print('foo')
    >>> ab(10, 20)                                              # doctest: +SKIP
    ______

    Часть 2
    >>> def bake(cake, make):                                   # doctest: +SKIP
    ...     if cake == 0:
    ...         cake = cake + 1
    ...         print(cake)
    ...     if cake == 1:
    ...         print(make)
    ...     else:
    ...         return cake
    ...     return make
    >>> bake(0, 29)                                             # doctest: +SKIP
    ______
    >>> bake(1, "беспонтовый пирожок")                          # doctest: +SKIP
    ______
    """
    return 0

# Вопрос 7.
def factors(n):
    """
    Выводит все числа, которые делят `n` без остатка.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 8.
def falling(n, k):
    """
    Вычисляет нисходящий факториал n глубины k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 9.
def double_eights(n):
    """
    Возвращает True, если в n содержится комбинация цифр 88.
    
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Ниже этого места трогать ничего не нужно.

if __name__ == '__main__':
    import doctest, sys
    finder = doctest.DocTestFinder()
    runner = doctest.DocTestRunner(doctest.OutputChecker(), optionflags=doctest.FAIL_FAST)
    doctest.OutputChecker.output_difference = lambda a, b, c, d: ""
    m = sys.modules.get('__main__')
    for test in finder.find(m, m.__name__):
        if test.name.split('.')[1][:2] != '_q': continue
        for example in test.examples: example.options[doctest.SKIP] = False
        if  runner.run(test).failed != 0: break