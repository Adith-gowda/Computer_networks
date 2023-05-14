def sender(l,n):
    print("\n***sender side***")
    sum1=0
    for i in range(0,n):
        sum1=sum1+l[i]
    print("sum is: ",sum1)
    return ~sum1
def receiver(l,ch,n):
    print("\n***receiver side***")
    sum2=0
    for i in range(0,n):
        sum2=sum2+l[i]
    print("sum is: ",sum2)
    sum2=sum2+ch
    print("checksum is: ",~sum2)

print("enter the number of frames: ")
n=int(input())
l=[int(input()) for i in range(n)]
ch=sender(l,n)
print("checksum is: ",ch)
receiver(l,ch,n)