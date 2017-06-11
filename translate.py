# encoding=utf8  
from textblob import TextBlob
import re

def check_contain_english(check_str):
    for en in check_str:
        if re.search('^[a-zA-Z]+$', en):
            return True
    return False
    
def translate(file_name):
    with open('static/en-us/' + file_name) as f:
        lines = f.readlines()
        lines = [l for l in lines if check_contain_english(l) ]  # english filter
        en_blob = TextBlob("".join(lines))
        return_str = en_blob.translate(to='zh')
        return_str = str(return_str).replace("。","。\n")
        return return_str
