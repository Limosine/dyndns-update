import requests
import os.path
import sys

cacheExec = False

def getIP():
    data = requests.get("https://ipinfo.io/json", verify = True).json()
    return data['ip']

def getURL(provider):
    urls = [
        '"https://update.spdyn.de/nic/update?hostname=" + hostname + "&myip=" + ip + "&user=" + username + "&pass=" + password',
        '"https://" + username + ":" + password + "@dynupdate.no-ip.com/nic/update?hostname=" + hostname + "&myip=" + ip',
    ]
    match provider:
        case "sp":
            return urls[0]
        case "noip":
            return urls[1]
        case _:
            print("Provider not yet supported.")
            print("Supported providers: Securepoint (sp), NoIP (noip)")
            sys.exit()

def readConfig(path):
    options = {
        "update": [],
    }
    configfile = open(path,  "r")
    while True:
        line = str(configfile.readline().strip())
        if not line:
            break
        elif line[-1] == "{":
            inOption = line.split()[0]
            options[inOption].append({})
            while True:
                line = str(configfile.readline().strip())
                if line == "}":
                    break
                else:
                    option = line.split(" = ")
                    options[inOption][-1][option[0]] = option[1]
        else:
            option = line.split(" = ")
            options[option[0]] = option[1]
    configfile.close()
    return options

def processConfig(options):
    for i in options["update"]:
        update(i["provider"], i["username"], i["password"], i["hostname"])

def cache(ip):
    global cacheExec
    if cacheExec == False:
        # cacheExec = True
        if os.path.exists("/tmp/dyndns-cache") == True:
            cachefile = open("/tmp/dyndns-cache", "r")
            ipold = str(cachefile.read())
            cachefile.close()
            if ip == ipold:
                print("IP hasn't changed.")
                # sys.exit()
        cachefile = open("/tmp/dyndns-cache", "w")
        cachefile.write(ip)
        cachefile.close()

def update(provider, username, password, hostname):
    ip = getIP()
    cache(ip)
    url = eval(getURL(provider))
    r = requests.post(url)
    print(r.content.decode())
