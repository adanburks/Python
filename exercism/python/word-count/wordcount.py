def word_count(phrase): # phrase is string; output is dictionary with word separated by # of occurrences
    import re
    length = len(phrase)
    print(length, re.findall(' ', phrase))
word_count("word is a word is a word")