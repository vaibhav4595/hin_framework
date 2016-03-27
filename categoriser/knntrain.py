from basicprocess import tokenizer
import json


def create_vectors(filename):
    idftokens = {}
    fw = open('categoriser/train_vectors.dat', 'w')
    fw2 = open('categoriser/train_vectors_idf.dat', 'w')
    fw3 = open('categoriser/train_cat.dat', 'w')
    fw4 = open('categoriser/train_number.dat', 'w')

    total_files = 0
    with open(filename) as fp:
        line = fp.readline()
        while line != '':
            serials = json.loads(line)
            if serials.has_key('mCategory'):
                total_files += 1
                tokens = tokenizer.string_tokenize(serials['text'])
                tftokens = {}
                for each in tokens:
                    if tftokens.has_key(each):
                        tftokens[each] += 1
                    else:
                        tftokens[each] = 1

                for each in tftokens.keys():
                    if idftokens.has_key(each):
                        idftokens[each] += 1
                    else:
                        idftokens[each] = 1
           
                fw.write(json.dumps(tftokens))
                fw.write('\n')
                fw3.write(serials['mCategory'])
                fw3.write('\n')

            line = fp.readline()

    fw2.write(json.dumps(idftokens))
    fw4.write(str(total_files))

    fw.close()
    fw2.close()
    fw3.close()
    fw4.close()
    fp.close()

create_vectors("categoriser/small_train.dat")
