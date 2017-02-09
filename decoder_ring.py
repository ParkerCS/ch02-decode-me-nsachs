# the three dimensional list below contains a secret message.
# each item in the list has a character (" " or "#") followed by a number representing the number of times you should print it.
# For instance, decode_me starts out with a ' ' printed 1 time, then a '#' printed 8 times etc.
# After printing all of the items in decode_me[i], you will
# need a carriage return before starting the next line.
# Decode and print the message.  You will know when you got it right.
# Good luck!
decode_me = [[[' ', 1], ['#', 8], [' ', 1], ['#', 8], [' ', 5], ['#', 3], [' ', 4], ['#', 2], [' ', 4], ['#', 2], [' ', 2], ['#', 6], [' ', 2], ['#', 4], [' ', 2], ['#', 6]], [[' ', 1], ['#', 2], [' ', 7], ['#', 2], [' ', 5], ['#', 2], [' ', 3], ['#', 2], [' ', 1], ['#', 2], [' ', 3], ['#', 3], [' ', 3], ['#', 2], [' ', 1], ['#', 2], [' ', 4], ['#', 2], [' ', 2], ['#', 2], [' ', 2], ['#', 2], [' ', 4], ['#', 2]], [[' ', 1], ['#', 2], [' ', 7], ['#', 2], [' ', 5], ['#', 2], [' ', 2], ['#', 2], [' ', 3], ['#', 2], [' ', 2], ['#', 4], [' ', 2], ['#', 2], [' ', 1], ['#', 2], [' ', 8], ['#', 2], [' ', 2], ['#', 2]], [[' ', 1], ['#', 6], [' ', 3], ['#', 8], [' ', 2], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 1], ['#', 2], [' ', 1], ['#', 2], [' ', 1], ['#', 2], [' ', 8], ['#', 2], [' ', 3], ['#', 6]], [[' ', 1], ['#', 2], [' ', 7], ['#', 2], [' ', 3], ['#', 2], [' ', 3], ['#', 9], [' ', 1], ['#', 2], [' ', 2], ['#', 4], [' ', 1], ['#', 2], [' ', 8], ['#', 2], [' ', 8], ['#', 2]], [[' ', 1], ['#', 2], [' ', 7], ['#', 2], [' ', 4], ['#', 2], [' ', 2], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 3], ['#', 3], [' ', 1], ['#', 2], [' ', 4], ['#', 2], [' ', 2], ['#', 2], [' ', 2], ['#', 2], [' ', 4], ['#', 2]], [[' ', 1], ['#', 2], [' ', 7], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 4], ['#', 2], [' ', 2], ['#', 6], [' ', 2], ['#', 4], [' ', 2], ['#', 6]], [[' ', 1], ['#', 8], [' ', 5], ['#', 3], [' ', 4], ['#', 8], [' ', 2], ['#', 2], [' ', 4], ['#', 2], [' ', 1], ['#', 8], [' ', 1], ['#', 8]], [[' ', 1], ['#', 2], [' ', 5], ['#', 2], [' ', 3], ['#', 2], [' ', 1], ['#', 2], [' ', 3], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 3], ['#', 2], [' ', 2], ['#', 2], [' ', 7], ['#', 2], [' ', 5], ['#', 2]], [[' ', 1], ['#', 2], [' ', 5], ['#', 2], [' ', 2], ['#', 2], [' ', 3], ['#', 2], [' ', 2], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 2], ['#', 2], [' ', 3], ['#', 2], [' ', 7], ['#', 2], [' ', 5], ['#', 2]], [[' ', 1], ['#', 8], [' ', 2], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 8], [' ', 2], ['#', 5], [' ', 4], ['#', 6], [' ', 3], ['#', 8]], [[' ', 1], ['#', 2], [' ', 8], ['#', 9], [' ', 1], ['#', 2], [' ', 3], ['#', 2], [' ', 3], ['#', 2], [' ', 2], ['#', 2], [' ', 3], ['#', 2], [' ', 7], ['#', 2], [' ', 3], ['#', 2]], [[' ', 1], ['#', 2], [' ', 8], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 4], ['#', 2], [' ', 2], ['#', 2], [' ', 3], ['#', 2], [' ', 2], ['#', 2], [' ', 7], ['#', 2], [' ', 4], ['#', 2]], [[' ', 1], ['#', 2], [' ', 8], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 4], ['#', 2], [' ', 1], ['#', 8], [' ', 1], ['#', 2], [' ', 5], ['#', 2]]]

#for i in range(len(decode_me)):
    #print(decode_me[i][1])


#print(decode_me[0][1])


for i in decode_me:
    for j in i:
        for k in range(j[1]):
            print(j[0], end = "")
    print()

