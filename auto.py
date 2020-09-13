import os, requests, getpass

os.system('clear')
print ("========================")
id = raw_input("Email : ")
pw = getpass.getpass(promt="Password : ")
print ("Checking Login...")

url = 'https://mobile.facebook.com/login.php'
headers = {
'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0',
'Accept-Laguage' : 'en-US,en;q=0.5'
}

data = {
'email' : id,
'pass' : pw
}

requests = requests.post(url, headers=headers, data=data).text

if "xc_message" in requests:
    print ("Berhasil login")
elif "checkpointSubmitButton" in requests:
    print ("Checkpoint")
else:
    print ("Login gagal")
