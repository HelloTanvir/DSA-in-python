# find the sum of digits of a positive integer number using recursion

def findSum(number):
    last_digit = number % 10
    new_number = number // 10

    if last_digit == number:
        return last_digit

    return last_digit + findSum(new_number)


number = int(input('enter a positive integer number: '))

sum = findSum(number)

print(f'the sum of all digits of the number: {sum}')
