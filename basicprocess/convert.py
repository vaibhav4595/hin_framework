import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

fp = open('data/Hindi.txt')
fw = open('data/help.txt', 'w')

lines = fp.readlines()

for i in xrange(0, 300000):
    fw.write(lines[i])
