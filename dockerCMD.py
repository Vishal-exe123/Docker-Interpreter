#!  /usr/bin/python3

import  cgi
import  subprocess

print("content-type:  text/html")
print("Access-Control-Allow-Origin: *")
print()

vishdata = cgi.FieldStorage()
cmd = vishdata.getvalue("x")

output = subprocess.getoutput("sudo  "+cmd)
print(output)
