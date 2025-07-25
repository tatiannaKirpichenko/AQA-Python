# разница в минутах между временными отметками
from asserts import assert_true


def time_diff(start_hour: int, start_minute: int, end_hour: int, end_minute) -> int:
    """

    :param start_hour: час первой отметки
    :param start_minute: минута первой отметки
    :param end_hour: час конечной отметки
    :param end_minute: минута конечной отметки
    :return:
    """

    start_total_minutes = start_hour * 60 + start_minute
    end_total_minutes = end_hour * 60 + end_minute

    if end_total_minutes < start_total_minutes:
        end_total_minutes += 24 * 60

    difference = end_total_minutes - start_total_minutes
    return difference


# =============================================
# блок проверки


assert_true(time_diff(1, 10, 1, 12) == 2)
assert_true(time_diff(1, 10, 2, 12) == 62)
assert_true(time_diff(2, 11, 2, 11) == 0)
assert_true(time_diff(2, 10, 2, 9) == 1439)
assert_true(time_diff(2, 10, 1, 12) == 1382)
assert_true(time_diff(2, 10, 1, 9) == 1379)