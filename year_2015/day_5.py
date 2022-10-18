import string


double_letters = [
    c * 2 for c in string.ascii_lowercase
]


def is_nice_level_1(data):
    vowels = 'aeiou'

    at_least_three_vowels = sum([
        data.count(c) for c in vowels if c in data
    ]) >= 3

    has_double_letters = sum([
        1 for dc in double_letters if dc in data
    ]) > 0

    blacklisted = ('ab', 'cd', 'pq', 'xy')

    has_not_blacklisted_strings = sum([
        1 for bc in blacklisted if bc in data
    ]) == 0

    return at_least_three_vowels and has_double_letters and has_not_blacklisted_strings


def level_1(input):
    return sum([
        1 for data in input.splitlines() if is_nice_level_1(data.strip())
    ])
