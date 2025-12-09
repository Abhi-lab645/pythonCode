"""
t=int(input())
for i in range(t):
    ls=list(map(int,input().split()))
    if len(set(ls))==1:
        print("YES")
    else:
        print("NO")
"""

q=int(int(input()))

for _ in range(q):
    n=int(input())
    s,t=input().split()
    result=True
    for ch in s:
        if (ch in t) and (s.count(ch)==t.count(ch)):
           continue
        else:
            result=False
            break

    if result:
        print("YES")
    else:
        print("NO")
