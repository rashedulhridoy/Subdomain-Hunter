import requests
import pyfiglet
import concurrent.futures


space =" "
print(space)

ascii_banner = pyfiglet.figlet_format("Sub Domain Hunter")
print(ascii_banner)
x = "Made By Rashedul Hridoy"
print(x)
print(space)
c = "Special Credit: Syed Sakib Alam Mubin, " + "Nabil Rahman"
print(c)
print(space)


domain = input("Enter Domain: ")


print(space)

print("-----Scanning Started-----")
print("> If You Find All Subdomains Then Tools With Automatic Stopped")

print(space)

"""
with open("Subdomain.txt", "r") as sub:
    subdomains = sub.read().splitlines()

    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(url)

            if response.status_code == 200:
                print(url)
                
                total_sub += 1

        except Exception as e: 
                pass
"""
o = open("Subdomain.txt","r",encoding="utf8").readlines()
def scan(x):
        total_sub = 0
        pay = x.strip()
        url_P = f"http://{pay}.{domain}"
        req = requests.get(url_P).status_code
        try:
           if req == 200:
              print(f"\033[1;32m[+] FOUND     : {url_P}")
              total_sub += 1
           else:
              print(f"\033[1;31m[!] NOT FOUND : {url_P}")
        except Exception as e:
              print(f"[+] ERROR : {e}")
              exit()
with concurrent.futures.ThreadPoolExecutor() as exe:
        exe.map(scan,o)
      

print(f"Scan Finished\nTotal Sub-Domain found: {total_sub}")
