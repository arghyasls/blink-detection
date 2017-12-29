def median(a):
    a.sort()
    if len(a)%2 !=0:
        return a[int(len(a)//2)]
    else:
        return ((a[int(len(a)//2)]+a[int(len(a)//2)-1])//2)

n=int(input())
import math
a=input().split(" ")
a=[int(i) for i in a]
a.sort()
if n%2!=0:
    print(median(a[:n//2]))
    print(median(a))
    print(median(a[n//2+1:]))
else:
    print(median(a[:n//2]))
    print(a[n//2])
    print(median(a[n//2:]))
    
    
  
    
    
n = int(input())
data = list(map(int, input().split()))
freq = list(map(int, input().split()))

s = []
for i in range(n):
    s += [data[i]] * freq[i]
N = sum(freq)
s.sort()

hr@codedata.io
info@codedata.io