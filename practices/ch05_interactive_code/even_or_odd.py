while True:

    number = int(input("Please provide a number: "))
    value = number % 2

    if number == 0:
        print(f"{number} was entered. See ya!")
        break
    elif value == False:
        print(f"{number} is even!")
    elif value == True:
        print(f"{number} is odd!")
    else:
        break