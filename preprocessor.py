import sys
import os
    
def read_words(words_file):
    return [word for line in open(words_file, 'r', errors='ignore') for word in line.split()]

fo=open(str(sys.argv[2]), "a")
dir=sorted(os.listdir(str(sys.argv[1])))
for fname in dir:
    fname1=str(sys.argv[1])+fname
    fname=fname.split('.')
    fo.write(fname[0]+" ")
    test=read_words(fname1)
    for word in test:
        word1=word.rstrip('\n')
        fo.write(word1+" ")
    fo.write("\n")
fo.close()
