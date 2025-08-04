import os

class Config(object):
####Dynamic Configs Variables (Don't Change)####
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    DB_NAME = os.environ.get("DB_NAME")
    
####Static Configs Variables(Changeable)####
    API_ID = 20535745 #API ID
    API_HASH = "d917a3ee53e8334d110e0c71e534b95d" #API HASH
    ADMIN_ID = 7780806801 #Admin ID
    DB_URL = "mongodb+srv://editingtution99:kLKimOFEX1MN1v0G@cluster0.fxbujjd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" #Database URL
    TXT_LOG = -1002733606326 #Text Log Channel ID
    LOG_CHANNEL = -1002733606326 #Log Channel ID
    CREDIT = "Bhavesh" #Credit Ko apne name se change kare
    PROXY = "103.172.85.194:50100" #Socks5 Proxy
    KEY = b'm88=p?h,u4*I>d.|XaiMg~.?\:2{Yr+~' #Key 
    IV = b'*}~&;&$;*:-![@&>' #IV

    TASK_LIMIT = 5 #Multiple Task Limit at 1 time
