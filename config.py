# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Rkn_Bots(object):
    # Rkn client config
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    #start_pic
    RKN_PIC = os.environ.get("RKN_PIC", "https://graph.org/file/e630eb748f7955d92c69a.jpg https://graph.org/file/3d6214e88828b2bb4caa0.jpg https://graph.org/file/5f62fb444889d8f393c23.jpg https://graph.org/file/176a6665a01c00cae8486.jpg https://graph.org/file/f6894089b82ff6b36a552.jpg https://graph.org/file/f880ed039bd0a8b504369.jpg")


    # wes response configuration
    BOT_UPTIME = time.time()
    PORT = int(os.environ.get("PORT", "8080"))
    FORCE_SUB = os.environ.get("FORCE_SUB", "") 
    
    # database config
    DB_NAME = os.environ.get("DB_NAME", "AutoCaption_V05_Bot")     
    DB_URL = os.environ.get("DB_URL", "")

    #caption
    DEF_CAP = os.environ.get("DEF_CAP",
                             "<b>@rb1official </b> <code>{file_name}</code><b>
╭────── • ◆ • ──────╮
✪ ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ:  <a href="https://t.me/rb1official">ʜᴇʀᴇ</a> ✪
╰────── • ◆ • ──────╯
=========== • ✠ • ===========
▫️ ᴄʜᴀɴɴᴇʟ : <a href="https://t.me/requestbox1officialofficial">ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>
▫️ sᴜᴘᴘᴏʀᴛ : <a href="https://t.me/helpsarthak_bot">ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>
=========== • ✠ • ===========</b>",
    )

    #sticker Id
    STICKER_ID = os.environ.get("STICKER_ID", "CAACAgUAAxkBAANCZh_bHUtmwoy2Q4pcJYqGyYD0uoIAApYDAALmW2hXq6HNrY1bPaceBA")

    #admin id
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
