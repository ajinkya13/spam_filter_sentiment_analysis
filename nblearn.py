import sys
import re

dict={}
wordcount={}
types={}
totalmsg=0
#"/home/ajinkya/Desktop/Assignment1/straining.txt"
for line in open(str(sys.argv[1]), "r", errors='ignore'):
#    temp=re.compile("[^\w]|_")
#    line=temp.sub(' ',line)
    line=line.rstrip('\n')
    l=line.split()
    t=l[1:]
    dict.setdefault(l[0], 0)
    dict[l[0]]=dict[l[0]]+1
    types[l[0]]='true'
    for word in t:
        dict.setdefault("COUNT"+l[0], 0)
        dict["COUNT"+l[0]]=dict["COUNT"+l[0]]+1
        dict.setdefault(l[0]+word, 0)
        dict[l[0]+word]=dict[l[0]+word]+1
        wordcount[word]='true'
fo=open(str(sys.argv[2]), "a")
#"/home/ajinkya/Desktop/Assignment1/smodel.txt"
fo.write("{\n")
for a,b in types.items():
    fo.write(str(a)+" "+str(dict[str(a)])+"\n")
    totalmsg=totalmsg+float(dict[str(a)])
fo.write("}\n")

fo.write("TOTALMSG "+str(totalmsg)+"\n")
fo.write("Vocabulary "+str(len(wordcount))+"\n")

for a,b in types.items():
    fo.write("COUNT"+str(a)+" "+str(dict["COUNT"+str(a)])+"\n")

for k,v in dict.items():
    fo.write(str(k)+" "+str(v)+"\n")

fo.close()