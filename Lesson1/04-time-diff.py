# разница в минутах между временными отметками
from asserts import assert_true


def time_diff(start_hour: int, start_minute: int, end_hour: int, end_minute) -> int:
    """

    :param start_hour: час первой отметки
    :param start_minute: минута первой  отметки
    :param end_hour: час конечной отметки
    :param end_minute: минута конечной отметки
    :return:
    """
    return 0


# =============================================
# блок проверки


assert_true(time_diff(1, 10, 1, 12) == 2)
assert_true(time_diff(1, 10, 2, 12) == 62)
assert_true(time_diff(2, 11, 2, 11) == 0)
assert_true(time_diff(2, 10, 2, 9) == 1439)
assert_true(time_diff(2, 10, 1, 12) == 1382)
assert_true(time_diff(2, 10, 1, 9) == 1379)