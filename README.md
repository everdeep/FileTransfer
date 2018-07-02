# FileTransfer
Small TCP app for transferring files between devices. Programmed in Python3.

To run the application, use python3 in the terminal and run the *client.py* file.
The local and external IP of the computer the client is being run on will be shown on the top of the window.
Input the IP of the device you want to send your files to in the destination text input on the top right.

You then need to enter a directory for where you want the files to be saved. It would be nice to get rid of
this and instead allow the other client to choose where to store it. The current method requires you knowing
the direct path and does not check if a folder or files have the same name as the files you are going to send,
and so it is possible that they will be overwritten.
