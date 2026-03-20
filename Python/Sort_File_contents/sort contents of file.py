fp=open("input.txt",'r')
word_lst=[]
for l in fp:
    word_lst+=l.split()
word_lst.sort()
str=" ".join(word_lst)
fp=open("output",'w')
fp.write(str)
fp.close()