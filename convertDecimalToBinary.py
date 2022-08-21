# convert a decimal number to a binary number using recursion

def convert(num):
    assert int(num) == num, 'The decimal number should be integer only'

    if num == 0:
        return 0

    divided = int(num / 2)
    rem = num % 2

    return rem + convert(divided) * 10


print(convert(-10))
