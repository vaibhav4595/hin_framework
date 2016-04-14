import sys
import math
import tokenizer
reload(sys)
sys.setdefaultencoding("utf-8")

punc_list = ['~', '`', '``', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '.', ',', '{', '}', '[', ']', '|', ':', '-']

def get_stop_list(filename, size):
    """
    Requires the filename as the argument
    Requires the number of stopwords required
    Filename should contain to text to find stop words
    returns a list of stop words
    """

    tokens = tokenizer.file_tokenize(filename)

    dic = {}

    for each in tokens:
        if dic.has_key(each):
            dic[each] += 1
        else:
            dic[each] = 1

    finaltup = sorted(dic.items(), key=lambda x:x[1], reverse=True)

    sendtup = []
    for each in finaltup:
        if (each[0] not in punc_list) and (each[0] != u'\u0964'):
            sendtup.append(each)

    return sendtup[:size]

def tf_stop_list(filename, size):
    """
    Requires the filename in the argument
    Specifically designed for cases when data has
        * json format
        * documents partitioned
    Returns a list of stopwords
    """

    freq = {}
    inv_freq = {}
    total = 0

    with open(filename) as fp:
        line = fp.readlines()
        while line != '':
            total += 1
            data = json.loads(line)
            tokens = tokenizer.string_tokenize(data['text'])
            tempdict = {}
            for each in tokens:
                if freq.has_key(each):
                    freq[each] += 1
                else:
                    freq[each] = 1
                tempdict[each] = True
            for each in tempdict.keys():
                if inv_freq.has_key(each):
                    inv_freq[each] += 1
                else:
                    inv_freq[each] = 1
            line = fp.readline()

    for each in freq.keys():
        factor = math.log(1 + (float(total) / float(inv_freq)))
        freq[each] = freq[each] * factor

    finaltup = sorted(freq.keys(), key=lambda x:x[1], reverse=True)

    sendtup = []
    for each in finaltup:
        if (each[0] not in punc_list) and (each[0] != u'\u0964'):
            sendtup.append(each)

    return sendtup[:size]
