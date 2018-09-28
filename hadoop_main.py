#!/usr/bin/python36
import cgi
import subprocess as sp
print("content-type:text/html")
print("\n")

print('''
<form action="hadoop_data_master.py">
  <p><b>Select your Datanode</b></p>
  <input type="checkbox" name="one" value="192.168.43.119">192.168.43.119<br>
  <input type="checkbox" name="one" value="192.168.43.28">192.168.43.28<br>
  <p><b>Select your name node</b></p>
  <input type="checkbox" name="two" value="192.168.43.111">192.168.43.111<br>
  <input type="submit">
''')

