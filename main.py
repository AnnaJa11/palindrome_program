my_word = input('Enter your word: ').lower()
if (my_word == my_word[::-1]):
    print(f'Your word: "{my_word}" is a palindrome.')
else:
    print(f'The word: "{my_word}" is NOT a palindrome.')