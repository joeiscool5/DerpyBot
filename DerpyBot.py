import discord 
from discord.ext import commands
from discord import app_commands
import sys
import time
from TOKEN import magicTOKEN


bot_testing_channel_id = 1406052132091854848

glazemode = False
glazeid: int = 1208411632103854091

class Client(commands.Bot):
    async def on_ready(self):
        global bot_testing_channel
        bot_testing_channel = client.get_channel(bot_testing_channel_id)

        print(f"connected to server as {self.user}!!!!!!!!!!!!!!!")
        
        try:
            guild = discord.Object(id=1265057220123431044)
            synced = await self.tree.sync(guild=guild)
            print(f'synced {len(synced)} commands to guild {guild.id}')

        except Exception as e:
            print(f'somthing: {e}')

    async def on_message(self, message):
        #if message.author == client.user:
        #    return
        
        print(message.author.id)

        cooluserid: int = 1208411632103854091
        karblarid: int = 795020647272284173
        if message.author.id == (glazeid) and glazemode:
            print("gng your so cool")
            await message.channel.send(f"you are like the coolest guy ever, did you know that")
        elif message.author.id == karblarid:
            await message.channel.send(f"ewww bro take a shower")
        
        new_message = message.content
        
        if new_message.startswith("Crazy?"):
            await message.channel.send(f"Crazy? I was crazy once, they locked me in a room a rubber room. A rubber room with RATS. And rats make me... CRAZY!")
        
        match new_message:
            
        
            
            
            case "Fortnight":
                picture = discord.File("Fortnight.gif")
                await message.channel.send(file = picture)

            case "School bathroom":
                picture = discord.File("ThousandYardStare.png")
                await message.channel.send(file = picture)
            
            case "School":
                picture = discord.File("ThousandYardStare.png")
                await message.channel.send(file = picture)
            
            case "boys bathroom":
                picture = discord.File("ThousandYardStare.png")
                await message.channel.send(file = picture)
            
            case "shutdown":
                
                await message.channel.send("gng ts does not work point and laugh, point and laugh")
    


intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)


GUILD_ID = discord.Object(id=1265057220123431044)

@client.tree.command(name ="shutdown", description="NO PLEASE DONT PLEASE", guild=GUILD_ID)
async def pingDerpy(interaction: discord.Interaction, supersecretpassword: str):
    if supersecretpassword == "bruh":
        await interaction.response.send_message("gng ts does not woafsrk")
        sys.exit(0)

@client.tree.command(name ="crazy", description="dont click please", guild=GUILD_ID)
async def pingDerpy(interaction: discord.Interaction):
    await interaction.response.send_message("Crazy?")

@client.tree.command(name ="glaze", description="you wanna be glazed?", guild=GUILD_ID)
async def pingDerpy(interaction: discord.Interaction):
    global glazemode
    global glazeid
    glazeid = interaction.user.id
    print(glazeid)
    if glazemode:
        glazemode = False
        await interaction.response.send_message("no more glaze for you")
    else:
        glazemode = True
        await interaction.response.send_message("Jarvis, activate glaze glaze?")

@client.tree.command(name ="lobotomy", description="lobotomy 101", guild=GUILD_ID)
async def pingDerpy(interaction: discord.Interaction):
    await interaction.response.send_message("https://en.wikipedia.org/wiki/Lobotomy")


client.run(magicTOKEN)