# Human Readable Time
def make_readable(seconds): 
    def single_digit(time):
        if time < 10:
            return('0'+str(time))
        else:
            return(str(time))
    
    hours = seconds//3600
    minutes = (seconds%3600)//60
    secs = seconds-(hours*3600)-(minutes*60)
    print(single_digit(hours)+':'+single_digit(minutes)+':'+single_digit(secs))
    
    
    




make_readable(0)
make_readable(5)
make_readable(60)
make_readable(86399)
make_readable(359999)













# Moving zeros to the end
def move_zeros(array):
    count = array.count(0)
    while 0 in array:
        array.remove(0)
    for i in range(count):
        array.append(0)
    return(array)


# move_zeros([1, 0, 1, 2, 0, 1, 3])





# Did I finish my Sudoku?

def done_or_not(board):
    nums = [1,2,3,4,5,6,7,8,9]



















#--------------------------------------#

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

# ROT13
import string
def rot13(message):
    
    def convert(alphabet_list, letter):
        index = alphabet_list.index(letter)
        new_index = index+13
        if new_index >= 26:
            new_index -= 26
        letter = alphabet_list[new_index]
        return letter
    new_string = ''
    lowercase = list(string.ascii_lowercase)
    #print(lowercase)
    uppercase = list(string.ascii_uppercase)
    #print(uppercase)
    letters = list(message)
    for letter in letters:
        if letter.isalpha() and letter.islower():
            new_string += convert(lowercase, letter)
        elif letter.isalpha() and letter.isupper():
            new_string += convert(uppercase, letter)
        else:
            new_string+=letter
    print(new_string)
    return new_string

# rot13('test')
# rot13('Test')
# rot13('Codewars')
# rot13('d')