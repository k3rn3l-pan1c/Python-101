pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    word = original.lower()
    first = word[0]
    print first
    new_word = word + first + pyg
    print new_word
    new_word = new_word[1:len(new_word)]
    print new_word
else:
    print 'empty'
