import requests
import re
import sys

def getdomains(domain):
        r = requests.get(f"https://crt.sh/?q={domain}")
        domains = []
        parsed = re.findall("<TD>(.*)</TD>",r.text)
        for line in parsed:
                splited = str(line).split("<BR>")
                for item in splited:
                        if len(item) > 3 and "<A style" not in item:
                                domains.append(item)
        clean = cleanup(domains)
        return clean

def cleanup(domains : list) -> list:
        return list(set(domains))

def main():
        if len(sys.argv) < 2:
                print("Usage: python crt.py domain")
                exit(0)
        domain = sys.argv[1]
        for d in getdomains(domain):
                print(d)

if __name__ == "__main__":
        main()