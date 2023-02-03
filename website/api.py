import urllib.request
import xml.etree.ElementTree as ET

class API:
    def __init__(self, link = None):
        self.link = link
        self.element = self.parse()

    def parse(self):
        if len(self.link) <= 0:
            raise ValueError("Steam id can't be 0 or less characters")
        
        link = self.link + "/?xml=1"
        with urllib.request.urlopen(link) as url:
            xml_data = url.read()
        
        root = ET.fromstring(xml_data)
        if root.text == None:
            raise ValueError("Custom steam id not found")
        
        return root

    def getSteamId64(self):
        return self.element.find("steamID64").text

    def getSteamId(self):
        return self.element.find("steamID").text

    def getStateMessage(self):
        return self.element.find("stateMessage").text

    def getAvatarFull(self):
        return self.element.find("avatarFull").text

    def getLocation(self):
        return self.element.find("location").text
    
    def getVacBans(self):
        return self.element.find("vacBanned").text

    def getOnlineState(self):
        return self.element.find("onlineState").text
    
    def getTradeBanState(self):
        return self.element.find("tradeBanState").text

    def getPlayedHours2Wk(self):
        return self.element.find("hoursPlayed2Wk").text

    def getMemberSince(self):
        return self.element.find("memberSince").text


if __name__ == "__main__":
    a = API("dggdlsakgslkgslgjkdgjkl")
    print(a.getAvatarFull())
    print(a.getLocation())
    print(a.getStateMessage())
    print(a.getSteamId())
    print(a.getSteamId64())


