import sys
import math
import re
from sys import stdout

dict={}
wordcount={}
classes={}
count=0
#"/home/ajinkya/Desktop/Assignment1/smodel.txt"
for line in open(str(sys.argv[1]), "r", errors='ignore'):
    line=line.rstrip('\n')
    l=line.split()
    if l[0]=='}':
        break
    if l[0]=='{':
        continue
    classes[l[0]]=l[1]
for k,v in classes.items():
    count=count+1
#    print(str(k)+" "+str(v))

for line in open(str(sys.argv[1]), "r", errors='ignore'):
    if count!=-2:
        count=count-1
        continue
    line=line.rstrip('\n')
    l=line.split()
#    print(l[0]+" "+l[1])
    dict[l[0]]=l[1]
#for k,v in dict.items():
#    print(str(k)+" "+str(v))
#print(dict['NEGon'])
#fo=open("/home/ajinkya/Desktop/Assignment1/sfinal.txt", "a")
#"/home/ajinkya/Desktop/Assignment1/straining.txt"
for line in open(str(sys.argv[2]), "r", errors='ignore'):
#    temp=re.compile("[^\w]|_")
#    line=temp.sub(' ',line)
    line=line.rstrip('\n')
    l=line.split()
    t=l[1:]
    prob=0
    tempprob=0
    predict=''
    for k,v in classes.items():
        tempprob=0
        for word in t:
            dict.setdefault(str(k)+word, 0)
#            print(str(k)+word+" "+dict[str(k)+word])
            tempprob=tempprob+math.log((float(dict[str(k)+word])+1)/(float(dict['COUNT'+str(k)])+float(dict['Vocabulary'])))
        tempprob=tempprob+math.log(float(dict[str(k)])/(float(dict["TOTALMSG"])))
        if prob==0:
            prob=tempprob
            predict=str(k)
        if tempprob>prob:
            prob=tempprob
            predict=str(k)
    sys.stdout.write(predict+"\n")
#    fo.write(predict+"\n")
#fo.close()