import json
from math import log, sqrt
from operator import itemgetter
from basicprocess import tokenizer
from collections import Counter

def knn_test(filename, k):
    """
    This function is meant to test the categories
    =============================================
    Requires : filename for testing
             : k - the number of neighbours to check for
    Along with this, it uses the followinf files
             * train_vectors.dat
             * train_vectors_idf.dat
             * train_cat.dat
             * tain_number.dat (stores the n for computation)
    =============================================
    """

    fw = open('categoriser/train_vectors_idf.dat')
    idftokens = json.loads(fw.readline())
    fw.close()

    fw = open('categoriser/train_number.dat')
    total_number = int(fw.readline())
    fw.close()

    fw = open('categoriser/train_cat.dat')
    catlist = fw.readlines()
    fw.close()    

    total_true = 0
    total = 0
    with open('categoriser/train_vectors.dat') as tf, open(filename) as fp:
        line = fp.readline()
        while line != '':
            terms = json.loads(line)
            if terms.has_key('mCategory'):
                idf_terms = set(tokenizer.string_tokenize(terms['text']))

                tf.seek(0, 0)
                line2 = tf.readline()

                total += 1
                similarity = []
                line_counter = 0

                while line2 != '':
                    tfvec = json.loads(line2)
                    score = 0

                    normaliser = 0
                    for each in idf_terms:
                        if idftokens.has_key(each):
                            if tfvec.has_key(each):
                                idfval = log(1 + (float((total_number)) / idftokens[each]), 2)
                                score += (idfval * tfvec[each])
                                normaliser += (tfvec[each] * tfvec[each])
                    normaliser = sqrt(normaliser)
                    score = score / normaliser

                    if len(similarity) < k:
                        similarity.append([score, line_counter])
                    else:
                        similarity.sort(key=itemgetter(0))
                        if similarity[0][0] < score:
                            similarity[0] = [score, line_counter]

                    line_counter += 1
                    line2 = tf.readline()

                finalcount = Counter()
                for each in similarity:
                    finalcount[catlist[each[1]]] += 1

                finallist = sorted(finalcount.items(), key=lambda x:x[1], reverse=True)
                print finallist[0][0].strip(), terms['mCategory']
                if finallist[0][0].strip() == terms['mCategory']:
                    total_true += 1

            line = fp.readline()
    print "Accuracy is ", (total_true / float(total)) * 100, "%"

knn_test('categoriser/small_test.dat', 5)
