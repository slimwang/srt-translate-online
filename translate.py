# encoding=utf8  
from textblob import TextBlob
import re


def is_num(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def check_contain_english(check_str):
    for en in check_str:
        if re.search('^[a-zA-Z]+$', en):
            return True
    return False

def translate(file_name):
    pieces = []
    try:
        with open('static/en-us/' + file_name) as f:
            str_array = []
            lines = f.readlines()
            for line in lines:
                if check_contain_english(line):
                    str_array.append(line)
            sentence = "".join(str_array).replace('\n', " ")
            
            # translate sentence
            en_sentence = TextBlob(sentence)
            zh_sentence = en_sentence.translate(to='zh')
            
            # insert back to en
            short_s = str(zh_sentence).replace('， ', " ").replace('。', ' ').replace('？', '？ ').split(" ")
            l_count = lines[-3] # line count
            print 'line count:' + l_count
            s_length = len(short_s)  # sentence length
            print 'sentence length: '+ str(s_length)
            p_length = int(float(s_length)/float(l_count))
            if p_length == 0:
                p_length += 1
            print 'piece length: ' + str(p_length)
            n = 0
            for i in range(len(lines)):
                if is_num(lines[i]):
                    print i
                    # final line
                    if i == l_count:
                        pieces.append(lines[i])
                        pieces.append(lines[i+1])
                        for j in range(n, s_length):
                            pieces.append(short_s[j] + '\n')
                    pieces.append(lines[i])
                    pieces.append(lines[i+1])
                    for j in range(n, n + p_length):
                        pieces.append(short_s[j] + '\n')
                    n = n + p_length
        
    finally:
        return " ".join(pieces)