import socket
import time
# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 9999
# connection to hostname on the port
clientsocket.connect((host, port))
# data to be sent
data = '21BAI1928'
# set the initial sequence number
seq_num = 0
# send data character by character
for char in data:
 # create the packet with sequence number and character
  packet = str(seq_num) + char
 
  while True:
 # send the packet to the server
    clientsocket.send(packet.encode())
 
 # set the timeout for receiving ACK
    clientsocket.settimeout(1)
 
    try:
      # receive ACK from the server
      ack = clientsocket.recv(1024).decode()
 
      # check if the ACK is for the correct sequence number
      if ack.startswith('ACK') and int(ack[3]) == seq_num:
        print('ACK received for sequence number: {}'.format(seq_num))
 
        # increment the sequence number
        seq_num = (seq_num + 1) % 2
 
        # exit the loop and send the next character
        break
      else:
        # resend the packet if the ACK is for the previous sequence number
        print('Resending packet: {}'.format(packet))
 
    except socket.timeout:
 # resend the packet if no ACK is received within the  timeout period
      print('Timeout occurred. Resending packet: {}'.format(packet))
 
# close the socket
clientsocket.close()