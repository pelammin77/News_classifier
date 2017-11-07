import glob
from nltk.tokenize import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer




def read_all_files(path):
    files = glob.glob(path)
    text = ""
    for file in files:
        #print(file)
        with open(file) as f:
            text += f.read()
    return text


def get_data_from_file(filename,tag = "sci"):
    a = []
    terms = open(filename, 'r').read()
    terms = terms.replace('of', '')
    terms = terms.replace('for', '')
    terms = terms.replace('is', '')
    terms = terms.replace('as', '')
    terms = terms.replace('to', '')
    terms = terms.replace('or', '')
    terms = terms.replace('the', '')
    terms = terms.replace('and', '')
    terms = terms.replace('in', '')
    for t in terms.split('\n'):
        if t == '':
            continue
        t = t.strip()
        t = t.lower()
       # for char in string.punctuation:
        #    t = t.replace(char, '')

        a.append((t, tag))
# train_terms.extend(a)
    print(a)
    print(len(train_terms))
    print(len(a))



def normalize_text(text):
    text = text.strip()
    text = text.lower()
    ps = PorterStemmer()
    stop_words = set(stopwords.words("english"))
    # print (stop_words)
    filtered_text = []
    stem_words = []
    words = word_tokenize(text)
    word_count = len(words)
    sents = sent_tokenize(text)
    sents_count = len(sents)
    for w in words:
        if w not in stop_words:
            filtered_text.append(w)
    for w in filtered_text:
        stem_w = ps.stem(w)
        stem_words.append(w)

    return stem_words
