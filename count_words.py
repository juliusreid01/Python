import re
from collections import Counter

def count_words(filename):
    """ For a given file this function prints the following
        - total number of words
        - top 20 most frequent words
        - occurrences of the top 20
    """
    fhand = open(filename, encoding='utf-8')
    text = fhand.read()
    lst = re.findall('\w+', text.lower())
    counts = Counter()
    
    # get count of each word
    for w in lst:
        counts[w] += 1
    
    print('Total number of words = ',len(lst))
    print('Top 20')
    
    # get the top 20
    for i in range(20):
        m = 0
        word = ''
        for w in counts.keys():
            if counts[w] > m:
                m = counts[w]
                word = w
        print('{}. {} occurrences of {}'.format(i+1, m, word))
        counts.pop(word)

    print('Easy Top 20')
    for w in counts.most_common(20):
        print(w[0], '\t', w[1])
        
count_words('shakespeare.txt')
#count_words_ans('roll_dice.py')
