my_word = input('Enter your word: ').lower()

def check_if_palindrome(word):
    if (word == word[::-1]):
        print('Your word is a palindrome.')
    else:
        print('The word is NOT a palindrome.')

check_if_palindrome(my_word)