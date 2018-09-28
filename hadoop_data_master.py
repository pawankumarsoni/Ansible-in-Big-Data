#!/usr/bin/python36
import cgi
#import os 
import subprocess as sp
print("content-type:text/html")
print("\n")

form=cgi.FieldStorage()
one=form.getvalue("one")
two=form.getvalue("two")
total_data=len(one)
total_name=len(two)
#print(type(one))
#print(one)
#print(two)
#print(len(one))

data_len=len(one)
name_len=len(two)
j=" ansible_ssh_user=root"+" "+"ansible_ssh_pass=pawan1997"
str="[data_ip]"+"\n"
if data_len is 14:
	str=str+one+j
else:
	for i in one:
		str=str+i+j+"\n"
str1="[name_ip]"+"\n"
if name_len is 14:
	str1=str1+two+j
print("<pre>")
#print(str)
#print(str1)
print("</pre>")
fh = open('/etc/ansible/hosts','a+')
fh.write({}.format(str))
fh.close()
sp.getoutput("echo"+" "+str+" "+">>"+" "+"/etc/ansible/hosts")
sp.getoutput("echo {} >> host_str.yml".format(str1))
sp.getoutput("hadoop namenode -format")
p=sp.getstatusoutput("sudo ansible-playbook /root/hadoop/hadoop_name_master.yml")
q=sp.getoutput("sudo ansible-playbook /root/hadoop/hadoop_data_name.yml")

#print(q[0])
#print(q[1])

print("yes")
