import re


def remove_vowels(string):
    return re.sub("[aeiouAEIOU]", "", string)


# using regular expression
