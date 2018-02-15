"""Looks for the given string is palindrome or not."""


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    return is_palindrome(middle(word))


def cancel_other_chars(word):
    new_word = ''
    word = word.lower()
    for i in word:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            new_word += i
    return new_word


print(is_palindrome(cancel_other_chars("Able was I ere I saw Elba")))
