import urllib
import urllib2
import json

def tokenize(sentence):
    """
    Connects to the ilmt pipeline
    ======
    returns the tokenized words along with sentence breakers
    uses ssf
    """

    src = "hin"
    target = "pan"

    SERVER="http://pipeline.ilmt.iiit.ac.in"
    TOKENIZER_URI = SERVER+ "/" + src + "/" + target + "/1/1/"

    values = {'input' : sentence.encode('utf-8'), 'params': {}}
    data = urllib.urlencode(values)

    f = urllib.urlopen(TOKENIZER_URI, data)
    tokenized = json.loads(f.read())

    return tokenized['tokenizer-1']
