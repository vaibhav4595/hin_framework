import json
from basicprocess import tokenizer

def get_categories(filename):
    final = {}
    with open(filename) as fp:
        line = fp.readline()
        while line != '':
            data = json.loads(line)
            if data.has_key('mCategory'):
                if not final.has_key(data['mCategory']):
                    final[data['mCategory']] = True
            line = fp.readline()
    for each in final.keys():
        print each,


def get_vocabulary(filename):
    vocab = {}
    nocat = 0
    with open(filename) as fp:
        line = fp.readline()
        while line != '':
            data = json.loads(line)
            if data.has_key('mCategory'):
                text = tokenizer.string_tokenize(data['text'])
                for each in text:
                    if not vocab.has_key(each):
                        vocab[each] = True
            else:
                nocat += 1
            line = fp.readline()
    print "Vocabulary Size is ", len(vocab)
    print "Number of articles which had no mCategory field were ", nocat

if __name__ == '__main__':
    get_categories('hi.data')
#    get_vocabulary('categoriser/hi.data')
