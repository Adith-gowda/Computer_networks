n=int(input())
l=[int(input()) for i in range(n)]
i=0
#finding the number of parity bits
for i in range(0,n):
    if (2**i)>=i+n+1 :
        break
tot=n+i
eve=[(2**j) for j in range(0,i)] #1,2,4,8
g=[]
for j in range(1,tot+1): 
    if j in eve:
        g.append(-1)
    else:
        g.append(j)
li=[list("0"*(i-len(bin(j)[2:])) + bin(j)[2:]) for j in range(1,tot+1)]
h=[];k=0
for j in range(len(g)):
    if g[j] != -1:
        g[j]=l[k]
        k=k+1
for k in range(i-1,-1,-1):
    li2=[]
    for j in range(len(li)):
        if li[j][k] == "1":
            li2.append(g[j])
    h.append(li2[1:].count(1))
# print(h)
for j in range(len(g)):
    if g[j] == -1:
        if(h[k]%2==0):
            g[j]=0
        else:
            g[j]=1
        k=k+1
print("Encoded data is: ",g) 