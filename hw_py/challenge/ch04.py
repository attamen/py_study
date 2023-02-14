o=input("염기 서열 입력>")
nucleos={
"a":0,
"t":0,
"g":0,
"C":0
}


for i in o:
    if i not in nucleos:
        nucleos[i]=0
    nucleos[i]+=1

for key in nucleos:
    print(f"{key}의 개수는 {nucleos[key]}")


    
