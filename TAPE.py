# https://codegolf.stackexchange.com/questions/157240/there-i-fixed-it-with-tape

alphabet = "abcdefghijklmnopqrstuvwxyz"
tape_string = "TAPETAPETAPETAPETAPETAPE"

string = raw_input("Enter a string to fix... with TAPE! ")

out_string = string[0]

for i in range(1, len(string)) :
    # Skip first character
    difference = alphabet.index(string[i]) - alphabet.index(string[i - 1])
    if difference > 1 :
        # Letters are not next to each other. Fix with TAPE!
        out_string += tape_string[ : difference - 1] + string[i]
    else :
        out_string += string[i]

print out_string
