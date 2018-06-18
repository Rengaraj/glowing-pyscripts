"""
Parser.py  parse http.log and sum the numbytes each unique IP.
"""
from collections import defaultdict

def  add_numbytes(data, ip, numbytes):
     """ add numbytes will find unique ip and sum the numbytes. if
     the ip is not present it will create the ip as key and assign 0 as
     default value. defaultdict() helps to do that.
     
     args:
         data - dictionary
         ip   -  ip as a key (string)
         numbytes - string

     returns:
            None
     """
     data[ip] = data[ip] + int(numbytes)
     
def main():
     """ open the log and read the file.
     Discard the first line and split split other lines in to a list.
     Then use only ip and numbytes from each line.
     """
     with open('http.log', 'r') as f:
          data = f.readlines()     

     data = data[1:]
     unique_ip = defaultdict(lambda: 0)

     for i in data:
          out = i.split()
          _ip, numbytes = out[1], out[4]
          
          add_numbytes(unique_ip, _ip, numbytes)

     print dict(unique_ip)

if __name__ == "__main__":
     main()

