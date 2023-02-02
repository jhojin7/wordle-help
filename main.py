# https://www.acmicpc.net/problem/24904
# https://upload.acmicpc.net/b1232df1-45d0-48e5-9129-82f0f16a9e95

import sys, os, string
f = open("words_boj.txt","r").read().split()
# words = {}
# for w in f:
#     words[w]=set(w.strip())
words = set(f)
alpha = set(string.ascii_uppercase)

green = set()
gray = set()
yellow = set()

def get_input(tries=1):
    if tries==0:
        print("wrong input;")
        exit()
    try:
        user_word,resp = input().split()
    except NameError or ValueError:
        print("try agaiin")
        get_input(tries-1)
    # resp = list(map(int,resp))
    return user_word, resp

def filter_one(user_word,resp):
    global words
    toremove = set()
    for i,ch in enumerate(user_word):
        if resp[i]=='0':
            # remove exact match
            if user_word in words:
                words.remove(user_word)
            # remove words with ch in word
            for word in words:
                if ch in word:
                    toremove.add(word)
        elif resp[i]=='1':
            gray.add(ch)
            # remove exact match
            if user_word in words:
                words.remove(user_word)
            # remove words with word[i]!=ch
            for word in words:
                # but if ch in word, continue
                if ch in word: 
                    continue
                if word[i]==ch:
                    toremove.add(word)
        elif resp[i]=='2':
            yellow.add(ch)
            # remove words with word[i]!=ch
            for word in words:
                if word[i]!=ch:
                    toremove.add(word)
    words -= toremove
    return green,yellow,gray

for _ in range(5):
    user_word, user_resp = get_input()
    print(user_word,user_resp,len(words))
    ret = filter_one(user_word,user_resp)
    print(ret)
    print(sorted(words)[:5])
