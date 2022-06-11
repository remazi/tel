import requests
import uuid
import sys
import os
from random import *
import colorama 
from colorama import * 
import random
# = = = = = = = = = = = = 

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[1;32m' #اخضر
A = '\033[2;34m'#ازرق داكن
C = '\033[1;35m' #وردي
B = '\033[1;36m'#سمائي
Y = '\033[1;34m' #ازرق
W ="\033[1;37m"#ابيض
# = = = = = = = = = = = =
print ("  ")
print (X+" 𝒊𝒏𝒔𝒕𝒂𝒈𝒓𝒂𝒎 𝒖𝒔𝒆𝒓 𝒕𝒐𝒐𝒍 𝒗2.0  ")
print (" ")
print (Z+" 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼: @𝙶_𝙳_𝙸   ")
print (" ")
print (B+"𝒊𝒏𝒔𝒕𝒂𝒈𝒓𝒂𝒎: @𝒛𝒗.𝒂𝒂 ")
banner = F
print(F+banner)
no = '1234567890'
abc = 'QAZWSXEDCRFVTGBYHNUJMIKLOP'
aab = 'QAZWSXEDCRFVTGBYHNUJMIKLOP'
po = '._'
ua = '1234567890'
a1n = '1234567890QAZWSXEDCRFVTGBYHNUJMIKOLP'
Extrra = 1
BGreen='\033[1;32m'
BRed ='\033[1;31m'
kwgd = '1'
pp = '5'
id = '5012751368'
tt = '5332779790:AAF1VfauHnzQnkEs5qDolLTEzNwON4fsSHY'
message = requests.get(f"https://api.telegram.org/bot{tt}/sendMessage?chat_id={id}&text= ⌔ New Start! ").json()
id_msg = str(message['result']["message_id"])
print()
ru = ('{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using a@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}')
def G():    
    if kwgd =='1':
        number = 0
        kumber = 0
        while True:
            a = ''.join(random.sample(abc, Extrra))
            n = ''.join(random.sample(no, Extrra))
            p = ''.join(random.sample(po, Extrra))
            an = ''.join(random.sample(a1n, Extrra))
            ar =  ''.join(random.sample(aab, Extrra))
            o = a + ar + p + n + n
            l = a + a + a + a + a + an
            k = a + n + p + a + n
            q = a + n + p + n + a
            e = n + a + p + a + n
            w = n + a + p + n + a
            f = a + ar + p + a + ar
            g = a + ar + p + ar + a
            v = n + an + p + a + n
            s = a + a + an + an + p
            x = a + a + a + a + a + an
            m = (o,l,q,e,w,f,v,s,x)
            us = ''.join(random.sample(m, Extrra))
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            heade={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 
#The data shown above are identical Do not touch anything developer Ruks          
            data={
                'email' : 'a@gmail.com',
                'username': f'{us}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
            da = requests.post(url,headers=heade,data=data).text
            if ru in  da:
                kumber+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n{us} | yes ",end='')                
                with open('insta.txt', 'a') as x:
                	x.write(us+ '\n')
                	tlg =(f'https://api.telegram.org/bot{tt}/sendMessage?chat_id={id}&text=\n NEW USER\n━━━━━━━━❪❂❫━━━━━━━━\n- 𝚄𝚂𝙴𝚁 : ( {us} )')           	
                	req = requests.post(tlg)             
                
            else:
                number+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n{us} | no  ",end='')                
                requests.post(f"""https://api.telegram.org/bot{tt}/editmessagetext?chat_id={id}&message_id={id_msg}&text=    
@G_D_I                 
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⌔ User : @{us} :
	
⌔️ Yes : @{kumber} :
⌔ No : @{number} :
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉""")

if kwgd == "2":
    webbrowser.open("https://t.me/G_D_I")                
if kwgd == "3":
	number = 0
	kumber = 0
	while True:
            t = random.choice(abc)
            p = random.choice(no)
            a = random.choice(po)
            us = t + t + t + a + p   
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            heade_ruks={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 
#The data shown above are identical Do not touch anything developer Ruks          
            data_ruks={
                'email' : 'a@gmail.com',
                'username': f'{us}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
            da = requests.post(url,headers=heade_ruks,data=data_ruks).text
            if ru in  da:
                kumber+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n جار الصيد \n[=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
                with open('insta.txt', 'a') as x:
                	x.write(us+ '\n')
                	tlg =(f'https://api.telegram.org/bot{tt}/sendMessage?chat_id={id}&text=\n NEW USER\n━━━━━━━━❪❂❫━━━━━━━━\n- 𝚄𝚂𝙴𝚁 : ( {us} )')           	
                	req = requests.post(tlg)             
                
            else:
                number+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n جار الصيد \n[=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
                
if kwgd == "4":
    number = 0
    kumber = 0
    while True:
            t = random.choice(abc)
            p = random.choice(an)
            a = random.choice(po)
            us = t + p + a + t + p 
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            heade_ruks={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 
#The data shown above are identical Do not touch anything developer Ruks          
            data_ruks={
                'email' : 'a@gmail.com',
                'username': f'{us}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
            da = requests.post(url,headers=heade_ruks,data=data_ruks).text
            if ru in  da:
                kumber+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n جار الصيد \n[=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
                with open('insta.txt', 'a') as x:
                	x.write(us+ '\n')
                	tlg =(f'https://api.telegram.org/bot{tt}/sendMessage?chat_id={id}&text=\n NEW USER\n━━━━━━━━❪❂❫━━━━━━━━\n- 𝚄𝚂𝙴𝚁 : ( {us} )')           	
                	req = requests.post(tlg)             
                
            else:
                number+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n جار الصيد \n[=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
if kwgd == "6":
    number = 0
    kumber = 0
    while True:
            u = str("".join(random.choice(abc)for i in range(1)))
            k = random.choice(no)
            j = random.choice(po)
            m = str("".join(random.choice(abc)for i in range(2)))
            us = k + j + k + m 
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            heade_ruks={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 
#The data shown above are identical Do not touch anything developer Ruks          
            data_ruks={
                'email' : 'a@gmail.com',
                'username': f'{us}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
            da = requests.post(url,headers=heade_ruks,data=data_ruks).text
            if ru in  da:
                kumber+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n جار الصيد \n[=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
                with open('insta.txt', 'a') as x:
                	x.write(us+ '\n')
                	tlg =(f'https://api.telegram.org/bot{tt}/sendMessage?chat_id={id}&text=\n NEW USER\n━━━━━━━━❪❂❫━━━━━━━━\n- 𝚄𝚂𝙴𝚁 : ( {us} )')           	
                	req = requests.post(tlg)             
                
            else:
                number+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n جار الصيد \n[=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')          
                
if kwgd == "5":
    number = 0
    kumber = 0
    while True:
            u = str("".join(random.choice(abc)for i in range(2)))
            k = random.choice(abc)
            j = random.choice(po)
            us = u + j + k + k
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            heade_ruks={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 
#The data shown above are identical Do not touch anything developer Ruks          
            data_ruks={
                'email' : 'a@gmail.com',
                'username': f'{us}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
            da = requests.post(url,headers=heade_ruks,data=data_ruks).text
            if ru in  da:
                kumber+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n جار الصيد \n[=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
                with open('insta.txt', 'a') as x:
                	x.write(us+ '\n')
                	tlg =(f'https://api.telegram.org/bot{tt}/sendMessage?chat_id={id}&text=\n NEW USER\n━━━━━━━━❪❂❫━━━━━━━━\n- 𝚄𝚂𝙴𝚁 : ( {us} )')           	
                	req = requests.post(tlg)             
                
            else:
                number+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n جار الصيد \n[=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
G()       
if kwgd == "7":
	print (Z+'    @HDDDDH     ')
if kwgd == "8":
	print ('    @RWKKK / ادخل هنا ضروري    ')