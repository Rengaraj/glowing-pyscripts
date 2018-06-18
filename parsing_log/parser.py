"""
Parser.py  parse http.log and sum the numbytes each unique IP.
"""

def  add_numbytes(data, ip, numbytes):
     """ add numbytes will find unique ip and sum the numbytes. if
     the ip is not present it will creat the ip as key and assign numbytes
     
     args:
         data - dictionary
         ip   -  ip as a key (string)
         numbytes - string

     returns:
            None
     """
     if data.has_key(ip):
         data[ip] = data[ip] + int(numbytes)
     else:
         data[ip] = int(numbytes)

def main():
     """ open the log and read the file.
     Discard the first line and split rest of the each line.
     Then use only ip and numbytes from each line.
     """
     with open('http.log', 'r') as f:
          data = f.readlines()     

     data = data[1:]
     unique_ip = {}

     for i in data:
          out = i.split()
          _ip, numbytes = out[1], out[4]
          
          add_numbytes(unique_ip, _ip, numbytes)

     print unique_ip

if __name__ == "__main__":
     main()

