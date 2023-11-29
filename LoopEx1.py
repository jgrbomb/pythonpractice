def main():
    # continue to run program until stop character is input('0')
    while True:
        # show a list of choices
        print("Enter the number for the function you'd like to run")
        choice = int(input("\t0.Exit Program\n\t1.String Palindrome\n\t2.Number Palindrome\n\t3.Sum of the Digits\nOption Number: "))
        # if input is 0 quit loop and exit program
        if choice is 0:
            print("Exiting Program...")
            break
        # first choice determines if a word is a palindrome
        elif choice is 1:
            StrPalindrome()
        # second choice determines if a number is a palindrome
        elif choice is 2:
            NumPalindrome()
        elif choice is 3:
        # third choices sums the digits of a number
            SumDigits()
        else:
            # invalid if choice is not a number or bigger than 3
            print("Invalid Choice Try Again")

def StrPalindrome():
    # user input for a word
    str = input("Enter Word: ")
    # copy of the reversed word
    temp = str[::-1]
    # makes both words all lower case
    # if the two strings are equal the word is a palindrome
    if temp.lower() == str.lower():
        print(str + " is a palindrome")
    # otherwise the word is not a palindrome
    else:
        print(str + " is not a palindrome")
def NumPalindrome():
    # user input for a number
    num = int(input("Enter an Integer: "))
    temp = num
    reversed = 0
    # creates a copy of the reversed digits
    while temp != 0:
        remainder = temp % 10
        reversed = reversed * 10 + remainder
        temp //= 10
    # if the two numbers are the same the number is a palindrome
    if reversed is num:
        print(str(num) + " is a numeric palindrome")
    # otherwise the word is not a palindrome
    else:
        print(str(num) + " is not a numeric palindrome")

def SumDigits():
    # user input for a number
    num = int(input("Enter an integer: "))
    temp = num
    sum = 0
    # removes each digits and adds it to the total sum
    while temp != 0:
        sum += temp % 10
        temp //= 10
    # prints the calculated sum
    print("The Sum of the Digits in " + str(num) + " is " + str(sum))

if __name__ == '__main__':
    main()