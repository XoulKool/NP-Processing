import socket                   # Import socket module
import time
import sys

fp = open('57log2.txt', 'a')
s1 = socket.socket()             # Create a socket object     # Get local machine name
port = 60001                    # Reserve a port for your service.
s1.bind(('10.100.0.6', port))
try:
    s1.connect(('10.100.0.7', port))
except (socket.error):
    s1.close()
    execfile('57client2.py')
s1.send("Server 6:  Hello server 7!")
f = open('received_file1', 'wb')
fp.write('Start:  ')
fp.write(str(int(time.time() * 1000)))
fp.write('\n')
print 'file 2 opened'
while True:
    data = s1.recv(4096)
    if not data:
        break
    f.write(data)
f.close()
fp.write('End:    ')
fp.write(str(int(time.time() * 1000)))
fp.write('\n')
print ('Successfully got file 2')
s1.close()
print ('Connection to server7 closed')

