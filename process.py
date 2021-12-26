fp = open("store.txt",'r',encoding='utf-8')
processedFile = open("processed.txt",'w',encoding='utf-8')
i=1;
for line in fp:
    line = " ".join(filter(lambda x:x[0]!='@', line.split()))
    line = " ".join(filter(lambda x:x[0:8]!="https://", line.split()))
    #line = " ".join(filter(lambda x:x, line.split(',')))
    processedFile.write(str(i)+". "+line+"\n")
    print(line)
    i+= 1
fp.close()
processedFile.close()

