def sentence(data):
    data=data.replace('?','.').replace('!','.').split('.')
    data = [title.strip() for title in data]
    data.pop()
    return data

def words(data):
    data=[title.lower().replace(',','').split(' ') for title in data]
    return data

# positive class training
from collections import Counter
d=Counter()
f=open("txt_sentoken/neg/output.txt","r")
content=f.read()
senten=sentence(content)
wordlist=words(senten)
wordcounter=0
for sen in wordlist:
    count=0
    megj=0
    for word in sen:
        if word!='' and word!='"' and word!='(' and word!=')'and word!=':'and word!=';'and word!='-':
            if megj==1:
                d["NOT_"+word]+=1
                count+=1
                wordcounter+=1
            else:
                d[word]+=1
                wordcounter+=1
            if word[-3:len(word)]=="n't":
                megj=1
            if count==2:
                megj=0
                count=0
Prob=Counter()
for word in d:
    Prob[word]=(d[word]+1)/(wordcounter+len(d))
Prob.most_common(10)


#negative class training
from collections import Counter
dpos=Counter()
f=open("txt_sentoken/pos/output.txt","r")
content=f.read()
senten=sentence(content)
wordlist=words(senten)
wordcounter=0
for sen in wordlist:
    count=0
    megj=0
    for word in sen:
        if word!='' and word!='"' and word!='(' and word!=')'and word!=':'and word!=';'and word!='-':
            if megj==1:
                dpos["NOT_"+word]+=1
                count+=1
                wordcounter+=1
            else:
                dpos[word]+=1
                wordcounter+=1
            if word[-3:len(word)]=="n't":
                megj=1
            if count==2:
                megj=0
                count=0
Probpos=Counter()
for word in dpos:
    Probpos[word]=(dpos[word]+1)/(wordcounter+len(dpos))
Probpos.most_common(10)


#testing the model on a new text file (movie review)
from collections import Counter
import math

dtest=Counter()
f=open("txt_sentoken/own_test.txt","r")
content=f.read()
senten=sentence(content)
wordlist=words(senten)
wordcounter=0
for sen in wordlist:
    count=0
    megj=0
    for word in sen:
        if word!='' and word!='"' and word!='(' and word!=')'and word!=':'and word!=';'and word!='-':
            if megj==1:
                dtest["NOT_"+word]+=1
                count+=1
                wordcounter+=1
            else:
                dtest[word]+=1
                wordcounter+=1
            if word[-3:len(word)]=="n't":
                megj=1
            if count==2:
                megj=0
                count=0

test_pos=0
test_neg=0
for word in dtest:
    if word in Probpos and word in Prob:
        test_pos+=math.log(Probpos[word])
        test_neg+=math.log(Prob[word])
    elif word in Probpos:
        test_pos+=math.log(Probpos[word])
    elif word in Prob:
        test_neg+=math.log(Prob[word])
if test_pos>test_neg:
    print("test_pos")
else: print("test_neg")
print(test_pos,test_neg)