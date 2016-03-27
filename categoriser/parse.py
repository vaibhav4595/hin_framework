import json


fw1 = open("small_test.dat", 'w')
fw2 = open("small_train.dat", 'w')

def parse_it(val1, val2):
    with open("hi.data") as fp:
        i = 0
        while i != val1:
            if i < val2:
                line = fp.readline()
                fw2.write(line)
            else:
                line = fp.readline()
                fw1.write(line)
            i += 1

#parse_it(201463, 161171)  #This one is meant for bigger tests
parse_it(1000, 800)
