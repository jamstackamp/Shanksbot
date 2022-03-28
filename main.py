digit = 0
divisor = 0
nextline = 1
counter = 1
i = 0
list_of_decimals = []
list_to_check = []
Answer = False

def check(Answer):
    i = len(list_to_check) - 1
    while i > 0:
        if nextline*10 == list_to_check[i]:
            return True

        else:
                i -= 1

divisor = input("\nEnter the prime number number you would like to test: ")

while (not Answer):

    digit = nextline*10//divisor
    list_of_decimals.append(digit)
    bottom = digit*divisor
    if check(Answer) == True:
        break
    else:
        list_to_check.append(nextline * 10)
        nextline = (nextline*10-bottom)
        counter +=1

print "\nThe number of digits that repeat are: "
print len(list_of_decimals)-2


