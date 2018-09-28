#!/usr/bin/python36
print("content-type:text/html")
print("\n")
import subprocess as sp
str="abcde"
p=sp.getstatusoutput("sudo echo {} >> /etc/ansible/hosts".format(str))
print(p[0])
print(p[1])

