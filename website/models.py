from . import dp 
from sqlalchemy import Column, String, Integer, create_engine
class SteamData(dp.Model):
    __tablename__ = "SteamData"

    id = dp.Column(dp.Integer, primary_key=True)
    customId = dp.Column(dp.String(100), unique=True)
    id64 = dp.Column(dp.String(20), unique=True)
    avatarURL = dp.Column(dp.String(150))
    location = dp.Column(dp.String(50))
    vacBans = dp.Column(dp.Integer)
    onlineState = dp.Column(dp.String(20))
    tradeBanState = dp.Column(dp.String(20))
    memberSince = dp.Column(dp.String(40))

    def __init__(self,
    id=None,
    customId=None,
    id64=None,
    avatarURL=None,
    location=None,
    vacBans=None,
    onlineState=None,
    tradeBanState=None,
    memberSince=None):
        self.id = id
        self.customId = customId
        self.id64 = id64
        self.avatarURL = avatarURL
        self.location = location
        self.vacBans = vacBans
        self.onlineState = onlineState
        self.tradeBanState = tradeBanState
        self.memberSince = memberSince
