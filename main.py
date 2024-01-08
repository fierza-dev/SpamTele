import aiohttp
import asyncio
import pyfiglet
import subprocess
from _.__.__ import *
from InquirerPy import prompt,inquirer

async def send_telegram(session, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
        "Content-Type": "application/json",
    }
    payload = {
        "chat_id": chat_id,
        "text": message,
    }
    async with session.get(url, headers=headers, json=payload) as response:
        return response
    
async def send_messages(session, message):
    while True:
        await send_telegram(session, message)

async def Spam():
    async with aiohttp.ClientSession() as session:
        message_to_send = input("Masukkan Pesan Kamu : ")
        response = await send_telegram(session, message_to_send)

        if response.status == 200:
            await send_messages(session, message_to_send)
        else:
            print(f"Failed to send message. Status code: {response.status}")
            print(await response.text())

def Setting():
    try:
        questions = [
            {
                'type': 'list',
                'name': 'SetConf',
                'message': 'Settings: ',
                'choices': [
                    'Token',
                    'Chat Id',
                    'Back To Menu'
                ]
            }
        ]

        answers = prompt(questions)

        if answers['SetConf'] == 'Token':
            SetToken = inquirer.text(message=f"Set Token > ").execute()
            config.set('TELEGRAM', 'token', SetToken)
            with open(config_path, 'w') as configfile:
                config.write(configfile)
            print("[ ! ] Successful Token Change...")
            Setting()
        elif answers['SetConf'] == 'Chat Id':
            SetChatId = inquirer.text(message=f"Set Chat Id > ").execute()
            config.set('TELEGRAM', 'chatid', SetChatId)
            with open(config_path, 'w') as configfile:
                config.write(configfile)
            print("[ ! ] Successful Chat Id Change...")
            Setting()
        else:
            main()
    except KeyboardInterrupt:
        choice = True
        choice = inquirer.confirm(message="Do you want to exit??", default=False).execute()
        exit() if choice else Setting()

def main():
    print(pyfiglet.figlet_format("Spam Tele"), end="Berfungsi Untuk Melakukan Spam Chat dengan Menggunakan Bot\n\n[@] Author: Fierza-Dev\n[-] Version : 1.0.0 ( Realese )\n\n")
    try:
        questions = [
            {
                'type': 'list',
                'name': 'menu',
                'message': 'Menu : ',
                'choices': [
                    'Spam Now',
                    'Setting',
                    'Exit'
                ]
            }
        ]

        answers = prompt(questions)

        if answers['menu'] == 'Spam Now':
            # Menjalankan event loop
            asyncio.run(Spam())
        elif answers['menu'] == 'Setting':
            Setting()
        elif answers['menu'] == 'Exit':
            print("[ >_< ] Good Bye....")
            exit()
    except KeyboardInterrupt:
        choice = True
        choice = inquirer.confirm(message="Do you want to exit??", default=False).execute()
        if choice:
            print("[ >_< ] Good Bye....")
            exit()
        else:
            main()

if __name__ == '__main__':
    try:
        main()
    except ImportError as err:
        subprocess.run("pip install -r requirements.txt",shell=True)