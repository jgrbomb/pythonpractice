while True:
    print("\tEnter the number for the function you'd like to run\n")
    choice = int(input("0.Exit Program\n1.String Palindrome\n2.Number Palindrome\n3.Sum of the Digits\n"))
    if choice is 0:
        break
    elif choice is 1:
        print("String Palindrome Func")
    elif choice is 2:
        print("Numeric Palindrome Func")
    elif choice is 3:
        print("Sum of the Digits Func")
    else:
        print("Invalid Choice Try Again")