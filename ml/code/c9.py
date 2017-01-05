import os
from time import sleep
import urllib.request
from urllib.error import HTTPError

import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.cross_validation import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn import grid_search

titles={}

titles['burton']=[4657, 2400, 5760, 6036, 7111, 8821,
                    18506, 4658, 5761, 6886, 7113]

titles['dickens']=[24022, 1392, 1414,1467,  2324, 580,
                     786, 888, 963, 27924, 1394, 1415, 15618,
                     25985, 588, 807, 914, 967, 30127, 1400,
                     1421, 16023, 28198, 644, 809, 917, 968, 1023,
                     1406, 1422, 17879, 30368, 675, 810, 924, 98,
                     1289, 1413, 1423, 17880, 32241, 699, 821, 927]

titles['doyle']=[2349, 11656, 1644, 22357, 2347, 290, 34627, 5148,
                   8394, 26153, 12555, 1661, 23059, 2348, 294, 355,5148,
                   5260, 8727, 10446, 126, 17398, 2343, 2350, 3070,
                   356, 5317, 903, 10581, 13152, 2038, 2344, 244, 32536,
                   423, 537, 108, 139, 2097, 2345, 24951, 32777, 4295,
                   7964, 11413, 1638, 21768, 2346, 2845, 3289, 439, 834]

titles['gaboriau']=[1748, 1651, 2736, 3336, 4604, 4002, 2451,
                      305, 3802, 547]

titles['nesbit']=[34219, 23661, 28804, 4378, 778, 20404, 28725,
                    33028, 4513, 794]

titles['tarkington']=[1098, 15855, 1983, 297, 402, 5798,
                        8740, 980, 1158, 1611, 2326, 30092,
                        483, 5949, 8867, 13275, 18259, 2595,
                        3428, 5756, 6401, 9659]

titles['twain']=[1044, 1213, 245, 30092, 3176, 3179, 3183, 3189, 74,
                   86, 1086, 142, 2572, 3173, 3177, 3180, 3186, 3192,
                   76, 91, 119, 1837, 2895, 3174, 3178, 3181, 3187, 3432,
                   8525]

url_base='http://www.gutenberg.org/files'
url_format='{url_base}/{id}/{id}-0.txt'

data_folder='../data/book/'

function_words = ["a", "able", "aboard", "about", "above", "absent",
                  "according" , "accordingly", "across", "after", "against",
                  "ahead", "albeit", "all", "along", "alongside", "although",
                  "am", "amid", "amidst", "among", "amongst", "amount", "an",
                    "and", "another", "anti", "any", "anybody", "anyone",
                    "anything", "are", "around", "as", "aside", "astraddle",
                    "astride", "at", "away", "bar", "barring", "be", "because",
                    "been", "before", "behind", "being", "below", "beneath",
                    "beside", "besides", "better", "between", "beyond", "bit",
                    "both", "but", "by", "can", "certain", "circa", "close",
                    "concerning", "consequently", "considering", "could",
                    "couple", "dare", "deal", "despite", "down", "due", "during",
                    "each", "eight", "eighth", "either", "enough", "every",
                    "everybody", "everyone", "everything", "except", "excepting",
                    "excluding", "failing", "few", "fewer", "fifth", "first",
                    "five", "following", "for", "four", "fourth", "from", "front",
                    "given", "good", "great", "had", "half", "have", "he",
                    "heaps", "hence", "her", "hers", "herself", "him", "himself",
                    "his", "however", "i", "if", "in", "including", "inside",
                    "instead", "into", "is", "it", "its", "itself", "keeping",
                    "lack", "less", "like", "little", "loads", "lots", "majority",
                    "many", "masses", "may", "me", "might", "mine", "minority",
                    "minus", "more", "most", "much", "must", "my", "myself",
                    "near", "need", "neither", "nevertheless", "next", "nine",
                    "ninth", "no", "nobody", "none", "nor", "nothing",
                    "notwithstanding", "number", "numbers", "of", "off", "on",
                    "once", "one", "onto", "opposite", "or", "other", "ought",
                    "our", "ours", "ourselves", "out", "outside", "over", "part",
                    "past", "pending", "per", "pertaining", "place", "plenty",
                    "plethora", "plus", "quantities", "quantity", "quarter",
                    "regarding", "remainder", "respecting", "rest", "round",
                    "save", "saving", "second", "seven", "seventh", "several",
                    "shall", "she", "should", "similar", "since", "six", "sixth",
                    "so", "some", "somebody", "someone", "something", "spite",
                    "such", "ten", "tenth", "than", "thanks", "that", "the",
                    "their", "theirs", "them", "themselves", "then", "thence",
                  "therefore", "these", "they", "third", "this", "those",
"though", "three", "through", "throughout", "thru", "thus",
"till", "time", "to", "tons", "top", "toward", "towards",
"two", "under", "underneath", "unless", "unlike", "until",
"unto", "up", "upon", "us", "used", "various", "versus",
"via", "view", "wanting", "was", "we", "were", "what",
"whatever", "when", "whenever", "where", "whereas",
"wherever", "whether", "which", "whichever", "while",
                  "whilst", "who", "whoever", "whole", "whom", "whomever",
"whose", "will", "with", "within", "without", "would", "yet",
"you", "your", "yours", "yourself", "yourselves"]

def get_data():
    for author in titles:
        print('Downloading titles from {author}'.format(author=author))
        author_folder=os.path.join(data_folder,author)
        if not os.path.exists(author_folder):
            os.makedirs(author_folder)
        for bookid in titles[author]:        
            print('----Getting book with id {id}'.format(id=bookid))
            url=url_format.format(url_base=url_base,id=bookid)
            print('----'+url)
            filename=os.path.join(author_folder,'{id}.txt'.format(id=bookid))
            if os.path.exists(filename):
                print('----File already exists, skipping')
            else:
                try:
                    urllib.request.urlretrieve(url,filename)                
                except HTTPError:
                    print('http error')
                sleep(60*10)
    print('Download completed!')

def clean_book(document):
    lines=document.split('\n')
    start=0
    end=len(lines)
    for i in range(len(lines)):
        line=lines[i]
        if line.startswith('*** START OF THIS PROJECT GUTENBERG'):
            start=i+1
        elif line.startswith('*** END OF THIS PROJECT GUTENBERG'):
            end=i-1
    return '\n'.join(lines[start:end])

def load_book_data():
    documents=[]
    authors=[]
    sub_folders=[subfolder for subfolder in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder,subfolder))]
    print(sub_folders)
    for author_number,subfolder in enumerate(sub_folders):
        full_sub_folder=os.path.join(data_folder,subfolder)
        for document_name in os.listdir(full_sub_folder):
            with open(os.path.join(full_sub_folder,document_name)) as inf:
                documents.append(clean_book(inf.read()))
                authors.append(author_number)
    return documents,np.array(authors,dtype='int')

def classify_document():
    documents,labels = load_book_data()

    extractor = CountVectorizer(vocabulary=function_words)
    parameters={'kernel':('linear','rbf'),'C':[1,10]}
    svc=SVC()
    grid=grid_search.GridSearchCV(svc,parameters)

    pipeline1= Pipeline([('feature_extraction',extractor),('clf',grid)])

    scores= cross_val_score(pipeline1,documents,labels,scoring='f1')
    print(np.mean(scores))

if __name__=='__main__':
    get_data()