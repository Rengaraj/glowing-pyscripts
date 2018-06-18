"""
ip:numbytes
"""
from collections import defaultdict

def  add_numbytes(data, ip, numbytes):
     if data.has_key(ip):
         data[ip] = data[ip] + int(numbytes)
     else:
         data[ip] = int(numbytes)

def main():
     with open('http.log', 'r') as f:
          data = f.readlines()     

     data = data[1:]
     unique_ip = {}

     for i in data:
          out = i.split()
          _ip, numbytes = out[1], out[4]
          
          add_numbytes(unique_ip, _ip, numbytes)

     print unique_ip

main()

