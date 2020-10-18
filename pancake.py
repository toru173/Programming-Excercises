# https://codegolf.stackexchange.com/questions/155650/can-you-outgolf-bill-gates


def sort (list) :
    for i in range(len(list)) :
        print i
        if i == 0 :
            continue 
        elif list[i] < list[i - 1] :
            print "Out of Order"
            stack = list[ : i ]
            pile = list[i : ]
            print stack, pile
            stack.reverse()
            list = stack + pile
            print list, stack + pile
    return list

list = [1, 2, 1]

print sort(list)
