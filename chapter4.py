#problem 4.27
def fcopy(original, copy):
    with open(original, 'r') as originalfile, open(copy, 'w') as copyfile:
       for line in originalfile:
           copyfile.write(line)

#problem 4.28
def links(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close
    return content.count('</a>')

#problem 4.29
def stats(filename):
    linecount = 0
    wordcount = 0
    charcount = 0
    infile = open(filename, 'r')
    for line in infile:
        line = line.strip("\n")
        words = line.split()
        linecount += 1
        wordcount += len(words)
        charcount += len(line)
    print ('line count: ' + str(linecount))
    print('word count: ' + str(wordcount))
    print('character count: ' + str(charcount + linecount))

#problem 4.31
def duplicates(filename):
    wordlist = []
    infile = open(filename, 'r')
    for line in infile:
        for words in line.split():
            if words not in wordlist:
                wordlist.append(words)
            else:
                return True
    return False

if __name__ == '__main__':
    fcopy('C:/Users/sanja/PycharmProjects/chapter3/example.txt', 'C:/Users/sanja/PycharmProjects/chapter3/output.txt')
    open('C:/Users/sanja/PycharmProjects/chapter3/output.txt').read()
    print(links('C:/Users/sanja/PycharmProjects/chapter3/html.txt'))
    stats('C:/Users/sanja/PycharmProjects/chapter3/example.txt')
    print(duplicates('C:/Users/sanja/PycharmProjects/chapter3/duplicates.txt'))
    print(duplicates('C:/Users/sanja/PycharmProjects/chapter3/noduplicates.txt'))