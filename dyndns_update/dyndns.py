import argparse
from getpass import getpass
import json
import os.path
import requests
import sys

def command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("provider", nargs="?", choices=["sp", "noip", "strato", "cloudflare"], help="Update a hostname by provider")
    parser.add_argument("-c", "--config", help="Specify a config file")
    parser.add_argument("-f", "--force", action="store_true", help="Disable cache")
    args = parser.parse_args()

    if args.provider:
        if args.provider == "cloudflare":
            api_email = input("API-Email: ")
            api_key = getpass("API-Key: ")
            zone_identifier = input("Zone-Identifier: ")
            identifier = input("Identifier: ")
            type = input("Type: ")
            hostname = input("Hostname: ")

            ip = getIP(True)
            updateCloudflare(ip, api_email, api_key, zone_identifier, identifier, type, hostname)
        else:
            username = input("Username: ")
            password = getpass()
            hostname = input("Hostname: ")

            ip = getIP(True)
            update(ip, args.provider, username, password, hostname)
    elif args.config:
        processConfig(args.config, args.force)
    else:
        if os.path.exists(os.path.expanduser("~/.config/dyndns-update/dyndns.cfg")):
            processConfig(os.path.expanduser("~/.config/dyndns-update/dyndns.cfg"), args.force)
        elif os.path.exists("/etc/dyndns-update/dyndns.cfg"):
            processConfig("/etc/dyndns-update/dyndns.cfg", args.force)

def getIP(force):
    print("getIP accessed")
    ipv4 = requests.get("https://ipv4.seeip.org/jsonip").json()['ip']
    ipv6 = None

    if os.path.exists("/tmp/dyndns-cache"):
        cachefile = open("/tmp/dyndns-cache", "r")
        ip = str(cachefile.read()).split(", ")
        cachefile.close()

        ipv4_cache = ip[0]

        if ipv4 == ipv4_cache and force != True:
            print("IP hasn't changed.")
            sys.exit()
        else:
            ipv4 = ipv4_cache
            ipv6 = ip[1]
    else:
        ipv6 = requests.get("https://ipv6.seeip.org/jsonip").json()['ip']

    cachefile = open("/tmp/dyndns-cache", "w")
    cachefile.write(ipv4 + ", " + ipv6)
    cachefile.close()

    return [ipv4, ipv6]

def getURL(provider):
    urls = [
        ['"https://update.spdyn.de/nic/update?hostname=" + hostname + "&myip=" + ip[0] + "," + ip[1] + "&user=" + username + "&pass=" + password', "get"],
        ['"https://" + username + ":" + password + "@dynupdate.no-ip.com/nic/update?hostname=" + hostname + "&myip=" + ip[0] + "," + ip[1]', "get"],
        ['"https://" + hostname + ":" + password + "@dyndns.strato.com/nic/update?hostname=" + hostname + "&myip=" + ip[0] + "," + ip[1]', "get"],
        ['"https://api.cloudflare.com/client/v4/zones/" + zone_identifier + "/dns_records/" + identifier', "put"],
    ]
    match provider:
        case "sp":
            return urls[0]
        case "noip":
            return urls[1]
        case "strato":
            return urls[2]
        case "cloudflare":
            return urls[3]
        case _:
            print("Provider not yet supported.")
            print("Supported providers: Securepoint (sp), NoIP (noip), STRATO (strato), Cloudflare (cloudflare)")
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
    ip = getIP(force)

    for i in options["update"]:
        if options["update"][i]["provider"] == "cloudflare":
            updateCloudflare(ip, options["update"][i]["api_email"], options["update"][i]["api_key"], options["update"][i]["zone_identifier"], options["update"][i]["identifier"], options["update"][i]["type"], options["update"][i]["hostname"])
        else:
            update(ip, options["update"][i]["provider"], options["update"][i]["username"], options["update"][i]["password"], options["update"][i]["hostname"])

def updateCloudflare(ip, api_email, api_key, zone_identifier, identifier, type, hostname):
    url = eval(getURL("cloudflare")[0])
    print(url)
    headers = {"Content-Type": "application/json", "X-Auth-Email": api_email, "X-Auth-Key": api_key}
    data = {
      "content": ip[0] if type == "A" else ip[1],
      "name": hostname,
      "type": type
    }
    r = requests.put(url, headers=headers, json=data)
    print(r.content.decode())

def update(ip, provider, username, password, hostname):
    url = eval(getURL(provider)[0])
    print(url)
    r = requests.get(url)
    print(r.content.decode())
