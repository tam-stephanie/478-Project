DIR_PATH = "sample_texts/"

import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import nltk
import VADER

# read the file
def process_file(fname):
    file_path = DIR_PATH + fname
    print(file_path)

    content = ""

    with open(file_path, 'r') as f:
        content = f.readlines()

    content = "".join(content)
    return content

# Test files
nltk.download('stopwords')
nltk.download('punkt')
engl_stops = nltk.corpus.stopwords.words('english')
symb_stops = [',','.','!','?',';',':','[',']','(',')']
engl_stops += symb_stops
#TODO: implement stopwords reduction

files = os.listdir(DIR_PATH)
sample_index = 0
file_chosen = files[sample_index]
words = process_file(file_chosen)
nltk.word_tokenize(words)

nltk.stem.snowball.SnowballStemmer("english")
