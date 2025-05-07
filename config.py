DISCORD_CLIENT_ID = "1369490472221020300"
DISCORD_CLIENT_SECRET = "kR6q6YnGiVH0Rh_Uz8T3XhhPmvHOjJCx"
DISCORD_REDIRECT_URI = "http://localhost:5000/callback"

API_BASE_URL = "https://discord.com/api"
OAUTH_AUTHORIZE_URL = f"https://discord.com/oauth2/authorize?client_id=1369490472221020300"
OAUTH_TOKEN_URL = f"https://discord.com/oauth2/authorize?client_id=1369490472221020300&permissions=8&response_type=code&redirect_uri=https%3A%2F%2Fdiscord.com%2Foauth2%2Fauthorize%3Fclient_id%3D1369490472221020300&integration_type=0&scope=identify+bot+guilds+applications.commands"

# Secret key for Flask sessions
SECRET_KEY = "a_very_secret_key_for_sessions"

# Webhook URL for bot verification endpoint
BOT_WEBHOOK_URL = "https://your-bot-server.com/verify"

# IPQualityScore API Key (optional)
IPQS_API_KEY = ""  # Add your key here if using VPN/proxy detection
