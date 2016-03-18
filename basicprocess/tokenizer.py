import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
import nltk


def file_tokenize(filename):
    """
    Takes filename as the argument
    ==============================
    Note : It is better to provide it with the absolute path
    Returns : a list of tokens
    Warning : May not be able to handle large files (reads all at once)
    """

    
    text = open(filename).read()
    text = text.decode("utf-8")

    # creates tokens using nltk module
    tokens = nltk.word_tokenize(text)

    return tokens

def string_tokenize(string):
    """
    Takes string as an argument
    ===========================
    Returns the list of tokens
    """

    text = string.decode("utf-8")

    tokens = nltk.word_tokenize(text)

    return tokens
