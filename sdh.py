import requests
import pyfiglet

total_sub = 0

space =" "
print(space)

ascii_banner = pyfiglet.figlet_format("Sub Domain Hunter")
print(ascii_banner)
x = "Made By Rashedul Hridoy"
print(x)
print(space)
c = "Special Credit: Syed Sakib Alam Mubin " + "Nabil Rahman"
print(c)
print(space)


domain = input("Enter Domain: ")


print(space)

print("-----Scanning Started-----")
print("> If You Find All Subdomains Then Tools With Automatic Stopped, Be Patient")

print(space)


with open("Subdomain.txt", "r") as sub:
    subdomains = sub.read().splitlines()

    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(url)

            if response.status_code == 200:
                print(f"\033[1;32m[+] FOUND : {url}")
                
                total_sub += 1

        except Exception as e: 
                print(f"\033[1;31m[!] NOT FOUND : {url}")

print("Scan Finished")
print(f"Total Sub-Domain found: {total_sub}")
