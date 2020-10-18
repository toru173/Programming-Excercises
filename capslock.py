# https://codegolf.stackexchange.com/questions/158132/no-a-just-caps-lock

input_string = raw_input("Without the notch, no one can hear you scream... ")

capslock_status = False
output_string = ""

def toggle_case(capslock_status, character) :
    if capslock_status is True :
        return character.swapcase()
    else :
        return character

for character in range(len(input_string)) :
    if input_string[character].lower() == 'a' :
        capslock_status = not capslock_status
    else :
       output_string += toggle_case(capslock_status, input_string[character])

print output_string
