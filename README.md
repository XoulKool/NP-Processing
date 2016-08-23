# NP-Processing

The test to be followed after AddFlow.   With this one we will be using at least three servers in conjunction with our controller server.
Just like the last test, be sure any flows on the table left behind are deleted before running the test by running command 

`ovs-ofctl del-flows br0`

on a Pica8 switch terminal. And again just a reminder this test uses OpenFlow 1.0 so if the Pica8 is not set to this be sure to do this with the command 

`ovs-vsctl set Bridge br0 protocols=OpenFlow10`

So to begin, we will need five different terminals for this test.  The first one will be the Pica8 OVS terminal, so ssh into that.  Then create another terminal ssh to grnlntrn.  Then create another one and ssh into server5 [10.0.0.5].  Then creae another one for server6 [10.0.0.6] and server7 [10.0.0.7] as well.  Now that we have these five terminal set up, we can try running the test

It is important to note that the whole purpose of this test is to see how quickly two roughly 1 GB files [both different]  can be transferred via a round-robin scheduling flow schedule.  In this case, there will be first access between servers 5 and 6 for three seconds then the flow wil halt and a flow will be added so that it will be server6 and server7's turn to exchange data.  At the end we will analyze the totaly time it took for both files to be completed.

On another note, please be sure you have created a file/s to be transferred and that the two listening servers know what these files are [see files 57Server1.py and 57Server2.py for comments on how to do this] 

