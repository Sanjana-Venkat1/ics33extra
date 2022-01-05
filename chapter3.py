import math

##problem 3.36
def reverse_int(holderint):
    if isinstance(holderint, int) == True:
        if holderint < 100 or holderint > 999 :
            print ("Not a valid input")
        else:
            holderstr = str(holderint)
            returnstr = holderstr[2] + holderstr[1] + holderstr[0]
            return returnstr
    else:
        print("Not a valid input")

#problem 3.37
def points(x1,y1, x2, y2):
    if (x2 - x1) == 0:
        distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
        print ('The slope is infinity and the distance is ' + str(distance))
    else:
        slope = (y2-y1)/(x2-x1)
        distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
        print ('The slope is ' + str(slope) + ' and the distance is ' + str(distance))

##problem 3.39
def collision(x1, y1, r1, x2, y2, r2):
    distancesq = (((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    radiussq = (r1 + r2) ** 2
    if distancesq > radiussq:
        return False
    else:
        return True

##problem 3.41
def lastF(FirstName, LastName):
    initial = FirstName[0]
    returnname = str(LastName) + ', ' + str(initial)
    return returnname

##problem 3.42
def avg(grades):
    for i in grades:
        counter = 0
        total = 0
        for j in i:
            total = total + j
            counter = counter + 1
        print(total/counter)

##problem 3.43
def hit(xc, yc, rc, xp, yp):
    if ((xp - xc) ** 2) + ((yp - yc) ** 2) <= rc ** 2:
        return True
    else:
        return False


if __name__ == '__main__':
    print(reverse_int(123))
    (points(0, 0, 1, 1))
    (points(0, 0, 0, 1))
    print(collision(0, 0, 3, 0, 5, 3))
    print(collision(0, 0, 1.4, 2, 2, 1.4))
    print(lastF('Albert', 'Camus'))
    avg([[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]])
    print(hit(0, 0, 3, 3, 0))
    print(hit(0, 0, 3, 4, 0))
