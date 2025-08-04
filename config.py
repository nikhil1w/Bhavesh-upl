import os

class Config(object):
####Dynamic Configs Variables (Don't Change)####
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    DB_NAME = os.environ.get("DB_NAME")
    
####Static Configs Variables(Changeable)####
    API_ID = 24660083 #API ID
    API_HASH = "4532ca1450d9e1bcc15267b964023ef2" #API HASH
    ADMIN_ID = 6801378994 #Admin ID
    DB_URL = "mongodb+srv://master:vwdBu3pYSaROoYcR@cluster0.zihv6vx.mongodb.net/" #Database URL
    TXT_LOG = -1002338959534 #Text Log Channel ID
    LOG_CHANNEL = -100233895944 #Log Channel ID
    CREDIT = "✞𝐑𝐚𝐎𝐧𝐞✞" #Credit Ko apne name se change kare
    PROXY = "103.172.85.194:50100" #Socks5 Proxy
    KEY = b'm88=p?h,u4*I>d.|XaiMg~.?\:2{Yr+~' #Key 
    IV = b'*}~&;&$;*:-![@&>' #IV
    TASK_LIMIT = 5 #Multiple Task Limit at 1 time