import sys
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

    # intialise dic for word count
    # TODO pending : exclude punctuation (define a punctuation list) 

    dic = {}

    for each in tokens:
        if dic.has_key(each):
            dic[each] += 1
        else:
            dic[each] = 1

    # the dictionary is sorted based on word frequency
    finaltup = sorted(dic.items(), key=lambda x:x[1], reverse=True)

    sendtup = []
    for each in finaltup:
        if (each[0] not in punc_list) and (each[0] != u'\u0964'):
            sendtup.append(each)

    return sendtup[:size]
