import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "21857983")
    API_HASH  = os.environ.get("API_HASH", "e469e84c943ce3b8b056eb6a296f2c67")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7508789523:AAE_0EYz7_E_FkI-hyXbtSnN5Axekmz-CqY") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://dhimanrajat:Y8IAGI0lVrMhjvkU@cluster0.mytkgu6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/nxK.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '833465134').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "aboutRizzx") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002497860595"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """<blockquote expandable>Hello {} 
    
➻ This Is An Advanced And Yet Powerful Rename Bot.
    
➻ Using This Bot You Can Auto Rename Of Your Files.
    
➻ This Bot Also Supports Custom Thumbnail And Custom Caption.
    
➻ Use /tutorial Command To Know How To Use Me.
    
<b>Bot Is Made By @ContactM_ebot</b></blockquote>"""
    
    FILE_NAME_TXT = """<blockquote expandable><b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ episode :- To Replace Episode Number
✓ quality :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S02 - EPepisode - quality  [Dual Audio] - @aboutRizzx </code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code></blockquote> """
    
    ABOUT_TXT = f"""<blockquote><b>
┏━━━━━━━━━━━━━
┣ 🔮 Creator        <a href='https://t.me/Noctophile'>𝙈𝙚</a>
┣ 🍄 Main Channel   <a href='https://t.me/aboutRizzx'>UPDATES </a>
┣ 🗿 Cloud Shop     <a href='https://t.me/vpsrdpdomainshop'>𝙑𝙋𝙎 | 𝗥𝗗𝗣 | 𝗗𝗼𝗺𝗮𝗶𝗻𝘀 ☁️</a>
┗━━━━━━━━━━━━━
</b></blockquote>"""

    
    THUMBNAIL_TXT = """<blockquote expandable><b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail</blockquote>"""

    CAPTION_TXT = """<blockquote expandable><b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption</blockquote>"""

    PROGRESS_BAR = """<blockquote>\n
<b>📁 Size</b> : {1} | {2}
<b>⏳️ Done</b> : {0}%
<b>🚀 Speed</b> : {3}/s
<b>⏰️ ETA</b> : {4} </blockquote>"""
    
    
    DONATE_TXT = """<blockquote><b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>🛍 UPI ID:</b> <code>mehere@sbi</code></blockquote> """
    
    HELP_TXT = """<blockquote expandable><b>Hey</b> {}
    
Here Is The Help For My Commands.</blockquote>"""





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper

