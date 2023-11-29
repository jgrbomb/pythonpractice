def main():
    # Runs until the issues inputs the esc character('0')
    while True:
        word = input("Enter a possible palindrome(Enter 0 to quit): ")
        if word == '0':
            print("Exiting Progam...")
            break
        # if the function returns true the word is a palindrome
        if palindrome(word):
            print("This word is a palindrome")
        # otherwise the word is not a palindrome
        else:
            print("This word is not a palindrome")

def palindrome(str):
    # if the string passed in is 1 or no letters long return true
    if len(str) < 2:
        return True
    # if the first and last letter do not match return false
    if str[0] != str[-1]:
        return False
    # if the first and last letter match remove the first and last letter 
    # and pass new string to funciton
    return palindrome(str[1:-1])
if __name__ == '__main__':
    main()