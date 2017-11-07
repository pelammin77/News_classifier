from textblob.classifiers import NaiveBayesClassifier
from data import *
import random
import glob
from nltk.tokenize import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
from preprocessing_data import *



'''
print(stopwords.words("english"))
w = newsTrain[10][0]
print(w)
wrd = 'Hi my name is Pete '
words = word_tokenize(wrd)
print(words)
print(newsTrain)
'''
#get_data_from_file("medi_train.txt",'medical')
text = read_all_files('entertainment/*')
normal_text = normalize_text(text)

random.shuffle(train_terms)
random.shuffle(test_terms)
cl = NaiveBayesClassifier(train_terms)

cl.show_informative_features(5)
print(cl.accuracy(test_terms))

result = cl.classify('Northern Ireland lost in Norway in their final world cup group game')
#print(cl.prob_classify(result))
print(result)

summary = '''At the NATO summit meeting in Warsaw last year, the allies, including the United 
States, agreed to fund the development of the Afghan security forces until the end of what 
was termed “the transition decade,” meaning from 2014, when Afghan forces began to take charge 
of their own security, until 2024. And the Green Zone in Baghdad has, its critics maintain, 
created an out-of-touch ruling class and Western community, and provided a magnet for protests 
while just moving enormous bombings elsewhere, further stoking popular discontent with leaders 
and foreigners. The military recently appointed an American brigadier general to take charge 
of greatly expanding and fortifying the Green Zone. Kabul’s Expanding Security Areas A protected 
area in Kabul, known as the Green Zone, will be expanded, and only official traffic will be
 permitted. KABUL Kabul International Airport Future Blue Zone Expanded Green Zone American 
 Embassy German Embassy Current Green Zone Kabul Kabul University AFGHANISTAN 1 mile KABUL
  Kabul International Airport Future Blue Zone Expanded Green Zone American Embassy German 
  Embassy Current Green Zone Kabul Kabul University AFGHANISTAN 1 mile KABUL Future 
  Blue Zone Expanded Green Zone American Embassy German Embassy Current Green Zone 1 
  mileUnlike Mr. Obama, Mr. Trump has suggested that American forces would remain in 
  Afghanistan until victory.'''
summary = summary.lower()
print(cl.classify(summary))
print ("Normal text:", normal_text)
#text = text.strip()
#text = text.lower()

#('', 'business'),
#('effective demand', 'business'),
#('effective tax rate', 'business'),
#('entrepreneur in heat', 'business'),
#result = cl.classify("I don't like their soup")
#print(result)
#ps = PorterStemmer()
#stop_words = set(stopwords.words("english"))
#print (stop_words)
#filtered_text = []
#stem_words = []
#words = word_tokenize(text)
#word_count = len(words)
#sents = sent_tokenize(text)
#sents_count = len(sents)
#for w in words:
 #   if w not in stop_words:
  #      filtered_text.append(w)
#for w in filtered_text:
 #   stem_w = ps.stem(w)
   # stem_words.append(w)

#print("Sent count", sents_count)
#print("Word count", word_count)
#print ("word count without sw", len(filtered_text))
#stem_words = set(stem_words)
#print ("stem:", stem_words)
#print(len(stem_words))

#print("all sents", sents)
