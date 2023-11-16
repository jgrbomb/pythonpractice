def main():
    while True:
        word = input("Enter a possible palindrome(Enter 0 to quit): ")
        if word == '0':
            print("Exiting Progam...")
            break
        if palindrome(word):
            print("This word is a palindrome")
        else:
            print("This word is not a palindrome")

def palindrome(str):
    if len(str) < 2:
        return True
    if str[0] != str[-1]:
        return False
    return palindrome(str[1:-1])
if __name__ == '__main__':
    main()