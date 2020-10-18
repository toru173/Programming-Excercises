# https://codegolf.stackexchange.com/questions/45550/print-a-block-diagonal-matrix

def buildLine(length, run, offset) :
    line = "0 " * offset
    line += "1 " * (run - 1) + "1"
    line += " 0" * (length - (offset + run))

    return line


input_string = raw_input("Enter a non-empty list of integers less than ten" + \
                         " (eg. 5 1 1 2 3 1): ")

# Tokenise and convert string to list of individual elements
dimensions = input_string.split()

# Convert list from strings to ints
dimensions = [int(i) for i in dimensions]

offset = 0

for i in range(len(dimensions)) :
    length = sum(dimensions)
    run = dimensions[i]

    for i in range(run) :
        print buildLine(length, run, offset)

    offset += run
