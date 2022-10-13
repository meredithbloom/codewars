
# PIG LATIN 
def pig_it(text):
    if len(text) == 0:
        return ''
    else:
        new = []
        words = text.split(' ')
        for word in words:
            if word.isalpha():
                word = word[1:]+word[0]+'ay'
                new.append(word)
            else:
                new.append(word)
        return " ".join(new)
        #print(new)

# print(pig_it('Pig latin is cool'))
# print(pig_it('Hello world !'))

#------------------------------------#
