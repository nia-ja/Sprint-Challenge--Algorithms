'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # if word is shorter then 2 letters we can't have there "th" for sure
    if len(word) < 2:
        return 0
    
    # look into first 2 letters
    if word[:2] == "th":
        # if there's "th" return count 1 + run recursion for the rest of the word
        return 1 + count_th(word[2:])
    else:
        # if there's no "th" return count 0 + run recursion for the rest of the word starting from the second letter
        return 0 + count_th(word[1:])