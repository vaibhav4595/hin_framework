import urllib
import urllib2
import json

def chunk(sentence):
    """
    Connects to the ilmt pipeline
    ======
    uses ssf
    """

    src = "hin"
    target = "pan"

    SERVER="http://pipeline.ilmt.iiit.ac.in"
    TOKENIZER_URI = SERVER+ "/" + src + "/" + target + "/1/5/"

    values = {'input' : sentence.encode('utf-8'), 'params': {}}
    data = urllib.urlencode(values)

    f = urllib.urlopen(TOKENIZER_URI, data)
    tokenized = json.loads(f.read())

    return tokenized['chunker-5']
