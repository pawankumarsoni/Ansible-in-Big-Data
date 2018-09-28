#!/usr/bin/python36
import cgi
import subprocess as sp
print("content-type:text/html")
print("\n")

print('''
<form action="map_job.py">
 <center> <p><b>Select your task tracker</b></p>
  <input type="checkbox" name="three" value="192.168.43.119">192.168.43.119<br>
  <input type="checkbox" name="three" value="192.168.43.28">192.168.43.28<br>
  <p><b>Select your job tracker</b></p>
  <input type="checkbox" name="four" value="192.168.43.111">192.168.43.111<br>
   <br />
  <input type="submit"></center>
''')
