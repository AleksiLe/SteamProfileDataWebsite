from flask import Blueprint, render_template, request, flash, jsonify
from .steamXMLparser import PROFILE
from .models import SteamData
from . import dp
import json
views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        steam_id = request.form.get('steam-id')
        if type(steam_id) == None:
            pass
        elif len(steam_id) == 0:
            flash("You didn't give steam id.", category="error")
        elif len(steam_id) < 20:
            flash("Your steam id is too short.", category="error")
        elif len(steam_id) > 98:
            flash("Your steam id is too long.", category="error")
        else:
            try:
                account = PROFILE(steam_id)
                data = SteamData.query.filter_by(id64 = account.getSteamId64()).first()
            except ValueError:
                flash("Your url was unknown type.", category="error")
                return render_template("index.html", steamdata = SteamData.query.all())
            if not data:
                print("New user")
                steamdata = SteamData(
                    id64 = account.getSteamId64(),
                    customId = account.getSteamId(),
                    avatarURL = account.getAvatarFull(),
                    location = account.getLocation(),
                    vacBans = account.getVacBans(),
                    onlineState = account.getOnlineState(),
                    tradeBanState = account.getTradeBanState(),
                    memberSince = account.getMemberSince())
                dp.session.add(steamdata)
                dp.session.commit()

    return render_template("index.html", steamdata = SteamData.query.all())

@views.route('/delete-steam_id', methods=['POST'])
def delete_steamId():
    steamdata = json.loads(request.data)
    steamdata_id = steamdata['steamdata_id'] 
    steamdata = SteamData.query.get(steamdata_id)
    if steamdata:
        dp.session.delete(steamdata)
        dp.session.commit()
        
    return jsonify({})

