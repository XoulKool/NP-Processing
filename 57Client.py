import socket                   # Import socket module
import time
import sys

i = 0
j = 0
fp = open('57log1.txt', 'a')
s = socket.socket()             # Create a socket object     # Get local machine name
port = 60000                    # Reserve a port for your service.
s.bind(('10.100.0.6', port))
try:
    s.connect(('10.100.0.5', port))
except (socket.error):
    s.close()
    execfile('57client.py')
s.send("Server 6:  Hello server 5!")
f = open('received_file', 'wb')
fp.write('Start:  ')
fp.write(str(int(time.time() * 1000)))
fp.write('\n')
print ('file 1 opened')
while True:
    data = s.recv(4096)
    if not data:
        break
    f.write(data)
f.close()
fp.write('End:    ')
fp.write(str(int(time.time() * 1000)))
fp.write('\n')
print ('Successfully got file 1')
s.close()
print ('Connection to server5 closed')

