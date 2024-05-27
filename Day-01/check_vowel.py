'''s=input()
for i in range(len(s)):
    if s[i] in "aeiouAEIOU":
        print(s[i].upper(),end="")
    else:
        print(s[i].lower(),end="") '''
 
s=input().lower()
vowels=set(list("aeiou"))
for i in range(len(s)):
    if s[i] in vowels:
        s=s[:i]+s[i].upper()+s[i+1:]
print(s)        