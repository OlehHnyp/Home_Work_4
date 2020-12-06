while 1:
    try:
        number = input("Please insert integer number:")
        if int(number) - float(number) == 0 and int(number) == abs(int(number)):
            break
    except ValueError:
        pass

up_border = int(number)
former_number = 0
next_number = 1
print(f"Here are Fibonacci numbers up to {up_border}:\n{former_number}", end=' ')
while next_number < up_border:
    print(next_number, end=' ')
    former_number, next_number = next_number, former_number + next_number

