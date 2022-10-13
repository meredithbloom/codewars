# Regex Password Validation - 5kyu
# You need to write regex that will validate a password to make sure it meets the following criteria:
# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a digit
# only contains alphanumeric characters (note that '_' is not alphanumeric)
from re import search 

regex = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*\d)[^\W_]{6,}$'

# start of word - ^
# contains at least one lowercase letter - (?=.*?[a-z])
# contains at least one uppercase letter - (?=.*?[A-Z])
# contains at least one number - (?=.*?[0-9]) - or (?=.*\d)
# only alphanumeric - [A-Za-z\d] -or  [^\W_]
# at least 6 characters long - {6,}
# end of word - $


# search(regex, 'fjd3IR9')
# search(regex, 'ghdfj32')
# search(regex, 'DSJKHD23')