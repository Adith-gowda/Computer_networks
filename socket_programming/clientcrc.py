import socket
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
        else:
          rem+='0'
          s=x(s,z)+d[i]
        i+=1
    if (s[0]=='1'):
        rem+='1'
    else:
        rem+='0'
    s=x(s,ds)
    ans=''
    print("\nquotient is: ",rem)
    print("\nremainder is: ",s)
    d=f+s
    return d

s=socket.socket()
p=12345
s.connect(('127.0.0.1',p))
d=input("get the data: ")
f=d
# ds='1001'
ds=input("\nget the key: ")
print("\n.................CRC CALCULATIONS.................")
d=d+'0'*(len(ds)-1)
z='0'*len(ds)
ans=crc(d,ds)
s.sendall(ans.encode())
s.sendall(f.encode())
s.sendall(ds.encode())
print(s.recv(1024).decode())
s.close()