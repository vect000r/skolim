import discord
import os
import asyncio
import yt_dlp
from dotenv import load_dotenv

class Skolim:
    def __init__(self):
        load_dotenv()
        self.AUTH_TOKEN = os.getenv('discord_token')
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        self.client = discord.Client(intents=self.intents)
        self.voice_clients = {}
        self.yt_dl_options = {"format": "bestaudio/best"}
        self.ytdl = yt_dlp.YoutubeDL(self.yt_dl_options)
        self.ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn -filter:a "volume=0.25"'}

    def run_bot(self):
        @self.client.event
        async def on_ready():
            print(f'{self.client.user} is now jamming')

        @self.client.event
        async def on_message(message):
            if message.content.startswith("?play"):
                try:
                    voice_client = await message.author.voice.channel.connect()
                    self.voice_clients[voice_client.guild.id] = voice_client
                except Exception as err:
                    print(err)
            
                try:
                    url = message.content.split()[1]

                    loop = asyncio.get_event_loop()
                    data = await loop.run_in_executor(None, lambda: self.ytdl.extract_info(url, download=False))

                    song = data['url']
                    player = discord.FFmpegOpusAudio(song, **self.ffmpeg_options)
                
                    self.voice_clients[message.guild.id].play(player)
                except Exception as err:
                    print(err)
        self.client.run(self.AUTH_TOKEN)
    

    def make_queue(self):
        pass
        #TODO
    

    def skip(self):
        pass
        #TODO


    def stop(self):
        pass
        #TODO
    