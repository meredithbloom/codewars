# The Hashtag Generator - 5 kyu
# all words must have first word capitalized, if final result is longer than 140 characters it must return false. if input or output is empty string, also return false
def generate_hashtag(s):
    if len(s.strip()) == 0:
        return False
    else:
        split_words = s.strip().split()
        new_string = '#'
        for i in range(len(split_words)):
            new_string += split_words[i].capitalize()
        if len(new_string) > 140:
            return False
        else:
            return(new_string)

       

# generate_hashtag('')
# generate_hashtag('Do We have A Hashtag')
# generate_hashtag('Codewars')
# generate_hashtag('Codewars      ')
# generate_hashtag('Codewars Is Nice')
# generate_hashtag('c i n')
# generate_hashtag('codewars  is  nice')
