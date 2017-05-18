import re
def my_map(in_file):
    wc = dict()
    for line in in_file:
        line = re.sub("[^A-Za-z0-9]"," ",line)
        words = line.split()
        for word in words:
            if(word in wc):
                wc[word]+=1
            else:
                wc[word]=1
    return wc