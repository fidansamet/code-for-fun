"""Returns True if a is power of b."""


def is_power(a, b):
    if a/b == 1.0:
        return True
    elif a % b == 0:
        return is_power(a / b, b)
    else:
        return False


if is_power(64,8):
    print('Yup')