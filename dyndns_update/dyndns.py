import requests
import os.path
import sys

cacheExec = False

def getIP():
    data = requests.get("https://ipinfo.io/json", verify = True).json()
    return data['ip']

def getURL(provider):
    if provider == "sp":
      return '"https://update.spdyn.de/nic/update?hostname=" + hostname + "&myip=" + ip + "&user=" + username + "&pass=" + password'
    elif provider == "noip":
      return '"https://" + username + ":" + password + "@dynupdate.no-ip.com/nic/update?hostname=" + hostname + "&myip=" + ip'
    else:
      print("Provider not yet supported.")
      print("Supported providers: Securepoint (sp), NoIP (noip)")

def cache(ip):
    global cacheExec
    if cacheExec == False:
        cacheExec = True
        if os.path.exists("/tmp/dyndns-cache") == True:
            cachefile = open("/tmp/dyndns-cache", "r")
            ipold = str(cachefile.read())
            cachefile.close()
            if ip == ipold:
                print("IP hasn't changed.")
                sys.exit()
        cachefile = open("/tmp/dyndns-cache", "w")
        cachefile.write(ip)
        cachefile.close()

def update(provider, username, password, hostname):
    ip = getIP()
    cache(ip)
    url = eval(getURL(provider))
    r = requests.post(url)
    print(r.content.decode())

# updateSP("***REMOVED***")
# updateSP("***REMOVED***")
# updateSP("***REMOVED***")
# updateNOIP("***REMOVED***")
# updateNOIP("***REMOVED***")
# updateNOIP("***REMOVED***")
