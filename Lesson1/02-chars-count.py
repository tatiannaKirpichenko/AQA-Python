
# Функция подсчета символа в строке
from asserts import assert_true


def chars_count(str_value: str, char: str) -> int:
    """

        :param str_value: строка, в которой ищем символм
        :param char: искомый символ
        :return: сколько раз символ встречается в строке
        """

    return str_value.count(char)


# =============================================
# блок проверки

assert_true(chars_count('12345', '0') == 0)
assert_true(chars_count('12345', '1') == 1)
assert_true(chars_count('12345qq', 'q') == 2)