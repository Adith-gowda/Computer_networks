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
    d=f+s
    return s

s=socket.socket()
print("socket created successfully....")
p=12345
s.bind(('',p))
print("binding to port: "%(p))
s.listen(5)
print('started listening MAX client: 5')
while True:
    c,addr=s.accept()
    print('got connection',addr)
    d=c.recv(1024).decode()
    data=c.recv(1024).decode()
    print("data received: ",data)
    key=c.recv(1024).decode()
    print("key received: ",key)
    f=d
    ds=key
    z='0'*len(ds)
    ans=crc(d,ds)
    print("................CRC VERIFICATION................\nquotient is:\nremainder is: ")
    if ans=='0'*(len(ds)-1):
        s.sendall("THANK you Data -> Received No error FOUND".encode())
    else:
        c.sendall("Error in data".encode())
    c.close()