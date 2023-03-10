import requests
import os.path
import sys
import argparse
from getpass import getpass

cacheExec = False

def command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("provider", nargs="?", choices=["sp", "noip"], help="Update a hostname by provider")
    parser.add_argument("-c", "--config", help="Specify a config file")
    parser.add_argument("-f", "--force", action="store_true", help="Disable cache")
    args = parser.parse_args()
    if args.provider:
        username = input("Username: ")
        password = getpass()
        hostname = input("Hostname: ")
        update(args.provider, username, password, hostname, args.force)
    if args.config:
        processConfig(args.config, args.force)

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
    def subOption():
        subOptions = {}
        while True:
                line = str(configfile.readline().strip())
                if not line:
                    break
                if line == "}":
                    break
                elif line[-1] == "{":
                    inOption = line.split()[0]
                    subOptions[inOption] = subOption()
                else:
                    option = line.split(" = ")
                    subOptions[option[0]] = option[1]
        return subOptions

    options = {}
    configfile = open(path,  "r")
    options = subOption()
    configfile.close()
    return options

def processConfig(path, force):
    options = readConfig(path)
    if "force" in options and force != True:
        force = eval(options["force"])
    for i in options["update"]:
        update(options["update"][i]["provider"], options["update"][i]["username"], options["update"][i]["password"], options["update"][i]["hostname"], force)

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

def update(provider, username, password, hostname, force):
    ip = getIP()
    if not force:
        cache(ip)
    url = eval(getURL(provider))
    r = requests.post(url)
    print(r.content.decode())
