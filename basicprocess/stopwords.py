import sys
import tokenizer
reload(sys)
sys.setdefaultencoding("utf-8")


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

    return finaltup[:size]
