from collections import defaultdict,Counter
s=defaultdict(int)
ip="abcd"
d="polikujmnhytgbvfredcxswqaz"
sol=""
for i in d:
    if i in ip:
        sol+=i*ip.count(i)
print(sol)