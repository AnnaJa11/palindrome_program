my_word = input('Enter your word: ').lower()

def check_if_palindrome(word):
    """
    takes input typed by user to check for palindrome, then reverses input and checks if input and reversed input are the same strings, and then prints the relevant answer.
    """
    if (word == word[::-1]):
        print('Your word is a palindrome.')
    else:
        print('The word is NOT a palindrome.')

check_if_palindrome(my_word)

