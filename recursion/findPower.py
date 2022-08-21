# find the power of a number using recursion

def findPower(base, exp):    
    assert exp >= 0 and int(exp) == exp, 'The exponent must be positive integer number'

    if exp == 0:
        return 1

    if exp == 1:
        return base

    return base * findPower(base, exp - 1)


power = findPower(2, 3)

print(f'the power is: {power}')
