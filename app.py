## File: app.py

from flask import Flask, redirect, request, session, url_for, render_template
import requests
from flask_session import Session
from config import *

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login")
def login():
    params = {
        "client_id": DISCORD_CLIENT_ID,
        "redirect_uri": DISCORD_REDIRECT_URI,
        "response_type": "code",
        "scope": "identify guilds"
    }
    url = f"{OAUTH_AUTHORIZE_URL}?{requests.compat.urlencode(params)}"
    return redirect(url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    data = {
        "client_id": DISCORD_CLIENT_ID,
        "client_secret": DISCORD_CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": DISCORD_REDIRECT_URI,
        "scope": "identify guilds"
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(OAUTH_TOKEN_URL, data=data, headers=headers)
    response.raise_for_status()
    token = response.json()["access_token"]

    user = requests.get(
        f"{API_BASE_URL}/users/@me",
        headers={"Authorization": f"Bearer {token}"}
    ).json()

    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    # Optional: VPN check with IPQualityScore
    if IPQS_API_KEY:
        vpn_check = requests.get(f"https://ipqualityscore.com/api/json/ip/{IPQS_API_KEY}/{ip}").json()
        if vpn_check.get("proxy") or vpn_check.get("vpn") or vpn_check.get("tor"):
            return "❌ VPN or Proxy detected. Please verify without one."

    # Notify the bot
    webhook_data = {
        "user_id": user["id"],
        "username": f"{user['username']}#{user['discriminator']}",
        "ip": ip
    }
    try:
        requests.post(BOT_WEBHOOK_URL, json=webhook_data)
    except:
        pass

    return render_template("verified.html", user=user, ip=ip)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
