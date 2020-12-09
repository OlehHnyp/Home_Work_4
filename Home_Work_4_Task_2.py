while 1:
    numbers_input = input("Please insert few integer numbers "
                          +"separated by space:"
                          )
    if numbers_input.replace(' ','').isdecimal() and numbers_input.find('.') == -1:
            break
    else:
        pass

numbers_list_float = [float(numbers_input.split()[i]) for i in range(len(numbers_input.split()))]

print("Here is a list with your numbers converted to the float type:\n",
      numbers_list_float, sep=''
      )