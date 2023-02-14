o=input("염기 서열 입력>")
count={}
for i in range(0,len(o),3):
    codon=o[i:i+3]
    if len(codon)==3:
        if codon not in count:
            count[codon]=0
        

        count[codon]+=1

print(count)
