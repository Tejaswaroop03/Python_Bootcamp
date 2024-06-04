st=input()
n=int(input())
str1=""
for i in st:
    ascii=ord(i)
    if n>=26:
        n=n%26
    if ascii-n<97:
        str1+=chr(122-(n-(ascii-96)))
    else:
        str1+=chr(ascii-n)         
print(str1)