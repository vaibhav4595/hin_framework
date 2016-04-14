import json
import random

fw1 = open("small_test.dat", 'w')
fw2 = open("small_train.dat", 'w')
fw3 = open("shuffled.dat", 'w')

def shuffle():
    lister = []
    with open("hi.data") as fp:
        line = fp.readline()
        while line != '':
            lister.append(line)
            line = fp.readline()
    random.shuffle(lister)
    for each in lister:
        fw3.write(each)

def parse_it(val1, val2):
    with open("shuffled.dat") as fp:
        i = 0
        while i != val1:
            if i < val2:
                line = fp.readline()
                fw2.write(line)
            else:
                line = fp.readline()
                fw1.write(line)
            i += 1


if __name__ == '__main__':
    print "Shuffling of data has begun"
    shuffle()
    print "Shuffling ended"

    #parse_it(201463, 161171)  #This one is meant for bigger tests
    print "creating files to be used for training and testing"
    parse_it(10000, 8000)
    print "==Process ended=="
