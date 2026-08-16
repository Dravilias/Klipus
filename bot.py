import discord
import os
from downloader import download_medal
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user}")


@tree.command(name="medal", description="Download a medal.tv clip")
async def medal(interaction: discord.Interaction, url: str):
    await interaction.response.defer()
    if not url.startswith("https://medal.tv") and not url.startswith("https://clips.medal.tv"):
        await interaction.followup.send("Link is not from medal")
        return 
    path = None
    try:
        path = await download_medal(url)    
        await interaction.followup.send(file=discord.File(path))
    except Exception as e:
        await interaction.followup.send(f"Error {e}")
    finally:
        if path and os.path.exists(path):
            os.remove(path)

client.run(token)