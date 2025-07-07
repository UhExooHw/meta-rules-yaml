import requests

urls = [
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn/hosts",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/hosts/ultimate.txt"
]

skip = {"localhost", "localhost.localdomain", "local", "broadcasthost",
        "ip6-localhost", "ip6-loopback", "ip6-localnet",
        "ip6-mcastprefix", "ip6-allnodes", "ip6-allrouters",
        "ip6-allhosts", "0.0.0.0"}

d = set()
for url in urls:
    r = requests.get(url)
    r.raise_for_status()
    for line in r.text.splitlines():
        if line.startswith(("0.0.0.0", "127.0.0.1")):
            parts = line.split()
            if len(parts) >= 2 and parts[1] not in skip and parts[1] != parts[0]:
                d.add(parts[1])

with open("ADS.yaml", "w", encoding="utf-8") as f:
    f.write("payload:\n")
    for domain in sorted(d):
        f.write(f"    - DOMAIN,{domain}\n")
