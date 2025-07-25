# Функция подсчета символа в строке без учета регистра
# Подсказка: используйте функцию lower

from asserts import assert_true


def chars_count(str_value: str, char: str, case_sensitive: bool) -> int:
    """

    :param str_value: строка, в которой ищем символм
    :param char: искомый символ
    :param case_sensitive: True - учитывать регистр, False - не учитывать
    :return: сколько раз символ встречается в строке
    """
    if not case_sensitive:
        str_value = str_value.lower()
        char = char.lower()

    return str_value.count(char)


# =============================================
# блок проверки


assert_true(chars_count('12345qQ', 'q', False) == 2)
assert_true(chars_count('12345qQ', 'Q', False) == 2)
assert_true(chars_count('12345qQ', 'q', True) == 1)
