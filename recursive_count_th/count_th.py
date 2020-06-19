'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# base case: when 'th' isn't found in the string
# if 'th' is in the string:
# call recursively, replace 'th' with a burrito on every pass
# return 1 to send back up the chain


def count_th(word):

    if "th" in word:
        return 1 + count_th(word.replace('th', '🌯', 1))
    else:
        return 0
