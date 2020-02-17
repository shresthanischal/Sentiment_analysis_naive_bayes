import csv
import spacy
from spacy.symbols import ADJ

nlp = spacy.load("en_core_web_sm")

p_word = []
n_word = []
pscore = 1.00
nscore = 1.00


with open('pdataset.csv','r') as f:
    reader = csv.reader(f)

    for row in reader:
        p_word.extend(row)

with open('ndataset.csv','r') as a:
    reader1 = csv.reader(a)

    for row in reader1:
        n_word.extend(row)

ip = input("Enter any statement:")

doc = nlp(ip)

#positive
for token in doc:
    for i in range(len(p_word)):
        if str(token) == p_word[i]:
            pscore = pscore * float(p_word[i+1])
        if token.pos_ == ADJ:
            pscore = pscore *(1-float(p_word[i+1]))

#negative
for token in doc:
    for i in range(len(n_word)):
        if str(token) == n_word[i]:
            nscore = nscore * float(n_word[i+1])
        if token.pos_ == ADJ:
            nscore = nscore *(1-float(n_word[i+1]))

if pscore > nscore:
    print("The statement is positive")
else:
    print("The statement is negative")
