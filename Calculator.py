def calculator(): #function
  while True: #looping will be running when it's true
    print("\n=== Calculator  ===")
    print("1. (+)")
    print("2. (-)")
    print("3. (*)")
    print("4. (/)")
    print("5. (%)")
    print("6. (^)")
    print("7. Exit")

    option = input("Choose option (1-7): ")
    # A condition for an exit
    if option == '7':
      print("Thanks for using this Calculator!")
      break

    # Conditions
    if option in ('1', '2' , '3' ,'4' , '5', '6'):
      try:
        number1 = float(input("Input first number: "))
        number2 = float(input("Inpur Second number: "))
      except ValueError:
        print("Error: Sorry... Input should be a number!")
        continue

      # What if condition
      if option == "1":
        result = number1 + number2
        print("The Result : ")
        print(f"{number1} + {number2} = {result}")

      elif option == "2":
        result = number1 - number2
        print("The Result : ")
        print(f"{number1} - {number2} = {result}")

      elif option == "3":
        result = number1 * number2
        print("The Result : ")
        print(f"{number1} * {number2} = {result}")

      elif option == "4":
        if number2 == 0:
          print("Error: Sorry, You cannot divide with zero")
        else:
          result = number1 / number2
          print("The Result : ")
          print(f"{number1} / {number2} = {result}")

      elif option == "5":
        result = number1 % number2
        print("The Result : ")
        print(f"{number1} % {number2} = {result}")

      elif option == "6":
        result = number1 ** number2
        print("The Result : ")
        print(f"{number1} ^ {number2} = {result}")

    else:
      print("Error: There's no option like that")
#Calling Function Calculator
calculator()