import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "22370385"))
    API_HASH = os.environ.get("API_HASH", "4051b5e638b4aa6af62c154efc4636b5")
    BOT_TOKEN = os.environ.get("8223356987:AAHrjC3NEL99xureyevoVmXsKlfQtAbPagg", None)
    STRING_SESSION = os.environ.get("BQE1hZwAbJKb1ipYhlTkK4cYNOVpCqAwt1LHJHKPdRG4-7XRpPG06ENHWc0JcvK4aFU177PDCwWZ2KPV_J0bM3HwiL6GyXrFJQPDuw7J8Nv3qzmUVU9mhMRQ_BguopsPpI_lxHHhWsxXDTaimBzGoYW9yrlk7qG2RFj9utCWzN-R7urP8gSgchR1-n4u_wb72gccEroX9M2zTLc5OoF_12KK4c0-KtaRePLvWUyX2oAb7_QNjKdXv1LQK8eIAmMALWMLml5vyVQXYe3YFcOPyu_q9IcTKMZP_INPACfEzysG94lObxmIqAtnYAQc9b7WyKXdThKkrY3-v2_jxI0TwS18pkL9bwAAAAFqejZeAAy", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("http://t.me/LamhaaMusicbot", "")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/Scooobygang") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/HoichoiZone") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://graph.org/file/0ab95ce4a7692f6d101de-40d13d71b0bbbb7666.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("6081361502", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
