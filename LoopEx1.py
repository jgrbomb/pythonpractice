def main():
    while True:
        print("Enter the number for the function you'd like to run")
        choice = int(input("\t0.Exit Program\n\t1.String Palindrome\n\t2.Number Palindrome\n\t3.Sum of the Digits\nOption Number: "))
        if choice is 0:
            print("Exiting Program...")
            break
        elif choice is 1:
            StrPalindrome()
        elif choice is 2:
            NumPalindrome()
        elif choice is 3:
            SumDigits()
        else:
            print("Invalid Choice Try Again")

def StrPalindrome():
    str = input("Enter Word: ")
    temp = str[::-1]
    if temp.lower() == str.lower():
        print(str + " is a palindrome")
    else:
        print(str + " is not a palindrome")
def NumPalindrome():
    num = int(input("Enter an Integer: "))
    temp = num
    reversed = 0
    while temp != 0:
        remainder = temp % 10
        reversed = reversed * 10 + remainder
        temp //= 10
    if reversed is num:
        print(str(num) + " is a numeric palindrome")
    else:
        print(str(num) + " is not a numeric palindrome")

def SumDigits():
    num = int(input("Enter an integer: "))
    temp = num
    sum = 0
    while temp != 0:
        sum += temp % 10
        temp //= 10
    print("The Sum of the Digits in " + str(num) + " is " + str(sum))

if __name__ == '__main__':
    main()