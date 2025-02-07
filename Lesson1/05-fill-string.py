# добавить между символами  строк подстроку
from asserts import assert_true


def fill_string(source_str: str, add_str: str) -> str:
    return add_str.join(source_str)


# =============================================
# блок проверки


assert_true(fill_string('abc', '1') == 'a1b1c')
assert_true(fill_string('abcd', '12') == 'a12b12c12d')
assert_true(fill_string('a', '1') == 'a')
