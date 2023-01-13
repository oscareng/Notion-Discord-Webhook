import requests

# URL of the webhook
WEBHOOK_URL_REVIEW = "https://discord.com/api/webhooks/1061741992448626729/xIbdIN2vJq7Ei99aMNYr-V5hYMUOwV6jeETR2sbzXOxssVhBFdE6bfg9WAx_kflU9u3t"
WEBHOOK_URL_APPROVED = "https://discord.com/api/webhooks/1061742548202311741/oqeg0KGQhUFeYXXEaSVBYEXSVP00t137ZZMJxMYdBpr6BhGW70r6sbgY-3ho6ShmmMKg"
# Function to send an embedded message with a hyperlink to the Discord channel
def send_embedded_message(title, description, url, color, fields):
    # Create the embed object
    embed = {
        "title": title,
        "description": "The following information was extracted from the Notion database:",
        "url": url,
        "color": color,
        "fields": fields,
    }

    # Create the request payload
    data = {"embeds": [embed]}

    # Send the POST request
    if "Approved" not in description:
        requests.post(WEBHOOK_URL_REVIEW, json=data)
        return
    else:
        requests.post(
            WEBHOOK_URL_APPROVED,
            json=data,
        )
        return
