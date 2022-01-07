import math

#problem 5.40
def approxPi(errorval):
    pi = math.pi
    divider = 1
    pireturn = 0
    counter = 0
    while abs(pi - pireturn) > errorval:
        if counter % 2 == 0:
            pireturn += 4/divider
        else:
            pireturn -= 4/divider
        divider += 2
        counter += 1
    return pireturn

#problem 5.41
def poly(values, x):
    returnvalue = 0
    exp = 0
    for i in values:
        returnvalue += (x ** exp) * i
        exp += 1
    return returnvalue

#problem 5.43
def evenrow(table):
    for i in table:
        if sum(i) % 2 == 1:
            return False
    return True

#problem 5.46
def inversion(string):
    counter = 0
    for i in range(len(string) - 1):
        for j in range(i+1, len(string)):
            if string[i] > string[j]:
                counter += 1
    return counter

#problem 5.48
def sublist(list1, list2):
    if list2 == [] and list1 != []:
        return False
    holder = 0
    lenlist2 = len(list2)
    for i in list1:
        while i != list2[holder]:
            holder += 1
            if holder == lenlist2:
                return False
        holder += 1
    return True



if __name__ == '__main__':
    print(approxPi(0.0000001))
    print(poly([1, 2, 1], 2))
    print(poly([1, 0, 1, 0, 1], 2))
    print(poly([1, 0, 1, 0, 1], 3))
    print(evenrow([[1, 3], [2, 4], [0, 6]]))
    print(evenrow([[1, 3, 2], [3, 4, 7], [0, 6, 2]]))
    print(evenrow([[1, 3, 2], [3, 4, 7], [0, 5, 2]]))
    print(inversion('ABBFHDL'))
    print(inversion('ABCD'))
    print(inversion('DCBA'))
    print(sublist([15, 1, 100], [20, 15, 30, 50, 1, 100]))
    print(sublist([15, 50, 20], [20, 15, 30, 50, 1, 100]))