import random

# function that takes in an array of sock colors and returns the number of pairs
def matchingSocks(ar):
    pairs = 0
    arset = set(ar) # creates a set from array
    for i in arset:
        # calculate pairs from total count of set elements in array
        pairs += int(ar.count(i) / 2)
    return pairs

print('\nTest 1')
print('-----------------------------------------')

test1 = [1,2,1,3,4,2,5,4,1,3]
print('Number of socks:',len(test1))
print('Array of colors:',test1)
print('\nPairs returned:',matchingSocks(test1))


# test the program of two different arrays 
print('\nTest 2')
print('-----------------------------------------')

# array1 has 30 elements and returns 10 pairs 
test2 = [random.randint(1,30) for i in range(30)]
while matchingSocks(test2) != 10:
    test2 = [random.randint(1,30) for i in range(30)]
print('Number of socks:',len(test2))
print('Array of colors:',test2)
print('\nPairs returned:',matchingSocks(test2))

print('\nTest 3')
print('-------------------------------------------')

# while array2 has 80 elements and has 36 pairs.
test3 = [random.randint(1,50) for i in range(80)]
while matchingSocks(test3) != 36:
    test3 = [random.randint(1,50) for i in range(80)]
print('Number of socks:',len(test3))
print('Array of colors:',test3)
print('\nPairs returned:',matchingSocks(test3),'\n')
