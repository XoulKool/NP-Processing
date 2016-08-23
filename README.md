# NP-Processing

The test to be followed after AddFlow.   With this one we will be using at least three servers in conjunction with our controller server.
Just like the last test, be sure any flows on the table left behind are deleted before running the test by running command 

`ovs-ofctl del-flows br0`

on a Pica8 switch terminal. And again just a reminder this test uses OpenFlow 1.0 so if the Pica8 is not set to this be sure to do this with the command 

`ovs-vsctl set Bridge br0 protocols=OpenFlow10`

So to begin, we will need five different terminals for this test.  The first one will be the Pica8 OVS terminal, so ssh into that.  Then create another terminal ssh to grnlntrn.  Then create another one and ssh into server5 [10.0.0.5].  Then creae another one for server6 [10.0.0.6] and server7 [10.0.0.7] as well.  Now that we have these five terminal set up, we can try running the test

It is important to note that the whole purpose of this test is to see how quickly two roughly 1 GB files [both different]  can be transferred via a round-robin scheduling flow schedule.  In this case, there will be first access between servers 5 and 6 for three seconds then the flow wil halt and a flow will be added so that it will be server6 and server7's turn to exchange data.  At the end we will analyze the totaly time it took for both files to be completed.

On another note, please be sure you have created a file/s to be transferred and that the two listening servers know what these files are [see files 57Server.py and 57Server2.py for comments on how to do this] 

To begin, run 57Server.py on Server 5 and 57Server2.py on Server7 to begin listening servers

Next, run simple_switch.py on grnlntrn server with command

`ryu-manager --verbose simple_switch.py`

The trickiest part is then running two programs as background processes on server 6.  Once the grnlntrn terminal has said that it has entered main mode, immediately run 

`python 57Client.py &`
followed by the command
`python 57Client2.py &`

and now you should see after about 6 seconds thing are happening in every terminal except for the Pica8 switch terminal.  Because the connection between server5 and server6 is given priority first, you should see the connection be successful between server5 and server6 first.  then after the three second time interval, the connection is interrupted and the connection is given between server6 and server7 to transfer data.

When everything is finished transferring, we are able to view how long each file took in UNIX epoch time by lookig at the files 57log1.txt [for file transferred from server 5 to server 6] and 57log2.txt [for file transferred from server6 to server7].  These times will be compared to the times in the next test.  

Again you may run this test as many times as you like, but keep in mind to delete any flows in the flow table after eac run to ensure consistent and quality test runs
