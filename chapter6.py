#problem 6.20
def reverse(phonebook):
    returndict = {}
    sorteddict = {}
    for key, value in phonebook.items():
        returndict[value] = key
    for i in sorted(returndict.items()):
        sorteddict[i[0]] = i[1]
    return sorteddict

#problem 6.21


#problem 6.25
def different(t):
    holderlist = []
    for i in t:
        for j in i:
            if j not in holderlist:
                holderlist.append(j)
    return len(holderlist)

#problem 6.27
def index(filename, wordlist):
    infile = open(filename, 'r')
    content = infile.readlines()
    infile.close()
    for i in wordlist:
        holderlist = []
        for line in range(len(content)):
            if i in content[line]:
                holderlist.append(line + 1)
        print(str(i) + '     ' + str(holderlist)[1:-1])


if __name__ == '__main__':
    phonebook = {'Smith, Jane': '123-45-67', 'Doe, John': '987-65-43', 'Baker,David': '567-89-01'}
    print(reverse(phonebook))
    print(different([[1,0,1], [0,1,0]]))
    print(different([[32, 12, 52, 63], [32, 64, 67, 52], [64, 64, 17, 34], [34, 17, 76, 98]]))
    index('raven.txt', ['raven', 'test'])