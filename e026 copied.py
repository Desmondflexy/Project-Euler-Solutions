def findSequenceLength(n):
    """Returns the length of the sequence provided by 1/n."""
    dividend = 1
    divisor = n
    pastRemainders = []
    while(True):
        remainder = dividend % divisor

        if(remainder in pastRemainders):
            return len(pastRemainders) - pastRemainders.index(remainder)

        if(remainder == 0): 
            return len(pastRemainders) - 1
            break

        pastRemainders.append(remainder)
        dividend = remainder * 10

#This is just a max value search pattern.
maxLength = 0
maxI = 0
for i in range(7, 1000, 2):
    if(i % 3 == 0 or i % 5 == 0): continue
    length = findSequenceLength(i)
    if(length > maxLength):
        maxLength = length
        maxI = i
print(maxI)
