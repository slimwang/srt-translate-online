# -*- coding: UTF-8 -*-
from textblob import TextBlob
import re

def translate(file_name):
    with open('static/en-us/' + file_name) as f:
        srt = f.readlines()
        en_blob = TextBlob(" ".join(srt))
        return_str = en_blob.translate(to='zh')
        return str(return_str)