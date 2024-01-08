import os
import configparser

config_path = os.path.join(os.getcwd(), "_","_", "_.ini")

def load_config(path):
    if os.path.exists(path):
        config = configparser.ConfigParser()
        config.read(path)
        return config
    else:
        print("File Config.ini Tidak Ada......")
        
config = load_config(config_path)
if config:
    bot_token = config.get('TELEGRAM', 'token')
    chat_id = config.get('TELEGRAM', 'chatid')
