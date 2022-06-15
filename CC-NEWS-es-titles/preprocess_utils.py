import re
import sys
import string
import unidecode

URLS_RE = re.compile(r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*')
DIGITS_RE = re.compile(r'[0-9]+')

def remove_urls(text):
    return URLS_RE.sub('', text)

def replace_multi_whitespaces(text):
    return ' '.join(text.split())

def remove_punctuation(text):
    return text.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))

def remove_others(text):
    base_ls = ["\xa0"]
    for i in base_ls:
        text = text.replace(i, " ")
    return text

def remove_accents(text):
    return unidecode.unidecode(text)

def replace_digits(text):
    return re.sub(DIGITS_RE,"DIGIT", text)

def remove_nonalphanum(text):
    return re.sub('[^a-zA-Z0-9]+', ' ', text)
                
def preprocess_text(text):
    text = text.lower()
    # text = remove_punctuation(text)
    text = remove_accents(text)
    text = remove_others(text)
    # text = replace_digits(text)
    text = remove_nonalphanum(text)
    text = replace_multi_whitespaces(text)
    return text
 