from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

init()

n = Fore.RESET
lg = Fore.BLUE
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
gr = Fore.GREEN
colors = [lg, r, w, cy, ye, gr]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    # fancy logo
    b = [
    

   ' ░█─░█ ░█─── ▀▀█▀▀ ░█▀▀█ ░█▀▀▀█ ░█▄─░█  ',
   ' ░█─░█ ░█─── ─░█── ░█▄▄▀ ░█──░█ ░█░█░█  ',
   ' ─▀▄▄▀ ░█▄▄█ ─░█── ░█─░█ ░█▄▄▄█ ░█──▀█ ',

    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    #print('=============SON OF GOD==============')
    print(f'   Version: 2.0 | Author: ULTRON{n}\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(lg+'[1] Delete  accounts'+n)
    print(lg+'[2] Filter Banned Accounts'+n)
    print(lg+'[3] Add  Accounts'+n)
    print(lg+'[4] exit'+n)
    a = int(input('\nEnter Your Choice: '))
    if a == 3:
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{gr} [~] Enter number of accounts to add in ultron: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{ye} [~] Enter Phone Number with country code: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{cy} [i] Saved all accounts in ULTRON')
            clr()
            print(f'\n{gr} [*] Logging in from new accounts\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 26377551 , 'cb5e6f090f9d5b3200475b88f7341709')
                c.start(number)
                print(f'{ye}[+] 𝐋𝐨𝐠𝐢𝐧 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮L')
                c.disconnect()
            input(f'\n Press enter to goto ultron menu...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] There are no accounts! Please add some and retry')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 8088717 , '7d1e0295ee1c2628f1933e9ffd2d8b78')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Enter the code: '))
                        print(f'{blue}[+] {phone} is not banned{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' is banned!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Congrats! No banned accounts')
                input('\nPress enter to goto ultron menu...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] All banned accounts removed'+n)
                input('\nPress enter to goto ultron menu...')

    elif a == 1:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{ye}[i] Choose an account to delete\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] Enter a choice: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Account Deleted{n}')
        input(f'\nPress enter to goto ultron menu...')
        f.close()
    elif a == 5:
        # thanks to github.com/thanosuser for the snippet below
        print(f'\n{lg}[i] Checking for updates...')
        try:
            # https://raw.githubusercontent.com/thanosuser/ULTRON-Adder/main/version.txt
            version = requests.get('https://raw.githubusercontent.com/thanosuser/ULTRON-Adder/main/version.txt')
        except:
            print(f'{r} You are not connected to the internet')
            print(f'{r} Please connect to the internet and retry')
            exit()
        if float(version.text) > 0.9:
            prompt = str(input(f'{lg}[~] Update available[Version {version.text}]. Download?[y/n]: {r}'))
            if prompt == 'y' or prompt == 'yes' or prompt == 'Y':
                print(f'{lg}[i] Downloading updates...')
                if os.name == 'nt':
                    os.system('del ULTRONadder.py')
                    os.system('del ULTRONmanager.py')
                else:
                    os.system('rm ULTRONadder.py')
                    os.system('rm ULTRONmanager.py')
                #os.system('del scraper.py')
                os.system('curl -l -O https://raw.githubusercontent.com/thanosuser/ULTRON-Adder/main/ULTRONadder.py')
                os.system('curl -l -O https://raw.githubusercontent.com/thanosuser/ULTRON-Adder/main/ULTRONmanager.py')
                print(f'{gr}[*] Updated to version: {version.text}')
                input('Press enter to exit...')
                exit()
            else:
                print(f'{lg}[!] Update aborted.')
                input('Press enter to goto ultron menu...')
        else:
            print(f'{lg}[i] Your Astra is already up to date')
            input('Press enter to goto ultron menu...')
    elif a == 4:
        clr()
        banner()
        exit()
