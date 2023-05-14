def x(a,b):
    s=''
    for i in range(len(b)):
        if a[i]==b[i]:
            s+='0'
        else:
            s+='1'
    return s[1:]
def crc(d,ds):
    rem='1'
    i=len(ds)
    s=d[0:i]
    while(i<len(d)):
        if s[0]=='1':
          rem+='1'
          s=x(s,ds)+d[i]
          print(s)
        else:
          rem+='0'
          s=x(s,z)+d[i]
          print(s)
        i+=1
    print(s," ",rem)
    if (s[0]=='1'):
        rem+='1'
    else:
        rem+='0'
    s=x(s,ds)
    print(s)
    d=f+s
    return d

d=input("get the data: ")
f=d
ds=input("\nget the key: ")
z='0'*len(ds)
d=d+'0'*(len(ds)-1)
ans=crc(d,ds)
print("endcoded data is ",ans)