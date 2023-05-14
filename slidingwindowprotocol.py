n=int(input())
l=[int(input()) for i in range(n)]
k=int(input())
windowsum=sum(l[:k])
maxsum=windowsum
for i in range(n-k):
    windowsum=windowsum-l[i]+l[i+k]
    maxsum=max(windowsum,maxsum)
print(maxsum)

#n=6
#1 5 8 2 7 9
#k=3