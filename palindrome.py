def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    digits = []
    digits_stack = []
    new_value = x

    while int(new_value / 10) >= 1:
        digits.append(new_value % 10)
        digits_stack.append(new_value % 10)
        new_value = int(new_value / 10)

    digits.append(new_value)
    digits_stack.append(new_value)

    for num in digits:
        if num != digits_stack.pop():
            return False

    return True
