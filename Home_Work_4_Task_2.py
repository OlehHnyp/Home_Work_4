while 1:
    numbers_input = input("Please insert few integer numbers "
                          +"separated by space:"
                          )
    if numbers_input.replace(' ','').isdecimal() and numbers_input.find('.') == -1:
            break
    else:
        pass

numbers_list = numbers_input.split()
for index in range(len(numbers_list)):
    numbers_list[index] = float(numbers_list[index])

print("Here is a list with your numbers converted to the float type:\n",
      numbers_list, sep=''
      )
