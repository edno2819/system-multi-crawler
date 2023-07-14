import discord
import logging

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)


class DiscordAlert:
    def __init__(self, server, channel, token):
        self.client = client
        self.client.run(token)
        self.server = server
        self.channel = channel
        self.token = token
        self.log = logging.getLogger(self.__class__.__name__)


    @client.event
    async def on_ready(self, msg):
        self.log.debug(f"Send report to {self.server}")
        for guild in client.guilds:
            if guild.name == self.server:
                break

        for channel in guild.channels:
            if channel.name == self.channel:
                break

        await channel.send(msg)
