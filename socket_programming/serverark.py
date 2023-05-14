import socket
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 9999
# bind to the port
serversocket.bind((host, port))
# queue up to 5 requests
serversocket.listen(5)
print('Server listening on {}:{}'.format(host, port))
while True:
  # establish a connection
  clientsocket, addr = serversocket.accept()
  print('Got a connection from {}'.format(addr))
 
  seq_num = 0
 
  while True:
    # receive data from the client
    data = clientsocket.recv(1024).decode()
 
    if not data:
      break
 
    # check the sequence number
    if int(data[0]) == seq_num:
      # send ACK to client
      ack = 'ACK' + str(seq_num)
      clientsocket.send(ack.encode())
 
    # print the received data
      print('Received: {}'.format(data[1:]))
 
    # increment the sequence number
      seq_num = (seq_num + 1) % 2
    else:
      # resend the ACK for the previous sequence number
      ack = 'ACK' + str((seq_num + 1) % 2)
      clientsocket.send(ack.encode())
      print('Resending ACK: {}'.format(ack))
# close the connection
clientsocket.close()