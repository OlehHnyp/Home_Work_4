count = int(input("How many Fibonacci numbers do you want to print? \n"))
fibonacci_list = [0, 1]
for i in range(2, count):
    fibonacci_list.append(fibonacci_list[i-2] + fibonacci_list[i-1])
fibonacci_list = [str(fibonacci_list[i]) for i in range(len(fibonacci_list))]
print("Here they are:",' '.join(fibonacci_list))