def ispali(i,j):
    if i>=j:
        return True
    if st[i]!=st[j]:
        return False
    return ispali(i+1,j-1)
st=input()
print(ispali(0,len(st)-1))