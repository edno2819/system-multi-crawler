from discord import SyncWebhook
import logging
import os

log = logging.getLogger(__name__)

webhook = SyncWebhook.from_url(os.getenv("WEBHOOK_URL"))

def send_msg(message):
    webhook.send(message)
