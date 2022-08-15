import requests
import re
import time
import random
import threading


file = open("proxylist.txt","w")
links = []
links.append("https://hidemy.name/tr/proxy-list/#list")

for i in range (64,9000,64):
    links.append(f"https://hidemy.name/tr/proxy-list/?start={i}#list")

def hidemyname(url):
    try:
        print(url)
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        time.sleep(random.uniform(1, 2))
        git = requests.get(url=url,headers=user_agent,timeout=5)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td><td>(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
    except:
        print("Hata Var")
        pass





for i in links:
    t1 = threading.Thread(target = hidemyname,args=(i,))
    time.sleep(0.1)
    t1.start()

    
