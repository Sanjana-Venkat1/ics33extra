#problem 7.19
def inValues():
    errorcount = 0
    sum = 0
    while errorcount < 2:
        value = input('Please enter a number: ')
        if value == '0':
            return sum
        try:
            sum = sum + float(value)
        except:
            errorcount +=1
            print('Error. Please re-enter the value')
    print("Two errors in a row. Quitting")



if __name__ == '__main__':
    print(inValues())