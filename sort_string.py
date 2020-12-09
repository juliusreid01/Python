def sort_string(s):
    """
    Sort the words in a string and return a string of words
    where the words are sorted (case-insensitive) but with same case
    e.g. str = "ORANGE banana apple"
    returns "apple banana ORANGE"
    """
    # create a dictionary to maintain original spelling
    words = dict()
    for w in s.split():
        k  = w.lower()
        ki = ''
        if k in words: ki = 0
        # this will allow duplicates with different spelling
        while (k + str(ki)) in words: ki = ki + 1
        # save the dictionary entry
        words[k + str(ki)] = w
    # now we can create and sort a list of those keys
    keys = list(words.keys())
    keys.sort()
    # now we can create a string of the original words using the sorted list
    retVal = ''
    for w in keys:
        retVal = retVal + words[w] + ' '

    return retVal.rstrip()

def sort_string_ans(s):
    words = s.split()
    # append lowercase copy to front of the words
    words = [w.lower() + w for w in words]
    # now sort
    words.sort()
    # array index to remove the copy from front
    words = [w[len(w)//2:] for w in words]
    return ' '.join(words)

print(sort_string("apple ORANGE banana"))
print(sort_string("world hello WorLd HelLo"))
