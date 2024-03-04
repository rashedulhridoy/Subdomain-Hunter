import requests
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Sub Domain Hunter")
print(ascii_banner)
x = "Made By Rashedul Hridoy"
print(x)
space =" "
print(space)

domain = input("Enter Domain: ")


print(space)

print("-----Scanning Started-----")
print("> If You Find All Subdomains Then Tools With Automatic Stopped")

print(space)


with open("Subdomain.txt", "r") as sub:
    subdomains = sub.read().splitlines()

    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(url)

            if response.status_code == 200:
                print(url)
                

        except Exception as e: 
                pass
                
                
                
