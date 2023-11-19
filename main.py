import time

import requests
import random,colorama
from colorama import Fore
import os
directory = "Carriers"

# Check if the directory exists
if not os.path.exists(directory):
    os.mkdir(directory)

# Check if the directory exists again
if os.path.exists(directory):
    pass
else:
    print("Making Dirs ....")
phone = open(input(f'''[+] Enter Number List  -->  ''')).read().splitlines()
apilayerapi = input(f'''[+] Enter Numverify API Key -->  ''')
for i in phone:
    from colorama import Fore
    colorama.init()
    greeen = Fore.GREEN
    white = Fore.WHITE
    url = f'https://apilayer.net/api/validate?access_key={apilayerapi}&number={i}&country_code=&format=1'
    sq = requests.get(url).json()
    phnumber = sq['number']
    carriers = sq['carrier']
    print(f'''{white}     {phnumber}               - {greeen}{carriers}''')
    with open(f"Carriers/{carriers} - Carrier.txt", 'a') as file:
        file.write(f'{i}\n')
time.sleep(3)