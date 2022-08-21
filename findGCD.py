# find GCD of 2 numbers

def findGCD(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integers'

    a = abs(a)
    b = abs(b)

    if a == 0: return b
    if b == 0: return a
    if a == b: return a

    max_num = max(a, b)
    min_num = min(a, b)

    return findGCD(min_num, max_num % min_num)


GCD = findGCD(48, 18)

print(f'the GCD is: {GCD}')
