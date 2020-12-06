while 1:
    try:
        number = input("Please insert a positive integer number:")
        if int(number) == abs(int(number)):
            break
    except ValueError:
        pass

# first way
number_int = int(number)
for dig in range(number_int)[1:]:
    number_int *= dig
number_factorial = number_int
print(f'Factorial of number {number} is {number_factorial}.')

# second way
factorial = int(number)
count = 2
while count < int(number):
    factorial *= count
    count += 1


# third way
digits_list = str(list(range(int(number) + 1)[1:])).strip('[]').split(',')
factorial_expression = '*'.join(digits_list)
evaluated_factorial = eval(factorial_expression)

print("It is realy true!") if number_factorial == factorial == evaluated_factorial else print("Or maybe not.")

