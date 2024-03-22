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
c = "Special Credit: Syed Sakib Alam Mubin"
print(c)
print(space)
z = "Modified Credit: Nabil Rahman"

print(z)

print(space)


domain = input("Enter Domain: ")


print(space)

print("-----Scanning Started-----")
print("> If You Find All Subdomains Then Tools With Automatic Stopped")

print(space)


o = open("Subdomain.txt","r",encoding="utf8").readlines()
def scan(x):
        
        pay = x.strip()
        url_P = f"http://{pay}.{domain}"
        req = requests.get(url_P).status_code
        try:
           if req == 200:
              print(f"\033[1;32m[+] FOUND     : {url_P}")
           else:
              print(f"\033[1;31m[!] NOT FOUND : {url_P}")
                
        except Exception as e:
              print(f"[+] ERROR : {e}")
              exit()
with concurrent.futures.ThreadPoolExecutor() as exe:
        exe.map(scan,o)
      

print("Scan Finished\n")
