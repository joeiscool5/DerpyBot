import discord 
from discord.ext import commands
from discord import app_commands
import sys
import time
from TOKEN import magicTOKEN


bot_testing_channel_id = 1406052132091854848

glazemode = False
glazeid: int = 1208411632103854091


GUILD_ID = discord.Object(id=1265057220123431044)



class Client(commands.Bot):
    
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)






        async def setup_hook(self):
        
            @bot.tree.command(name ="shutdown", description="NO PLEASE DONT PLEASE")
            async def pingDerpy(interaction: discord.Interaction, supersecretpassword: str):
                if supersecretpassword == "bruh":
                    await interaction.response.send_message("gng ts does not woafsrk")
                    sys.exit(0)
                else:
                    await interaction.response.send_message("You are so stupuid")

            @bot.tree.command(name ="crazy", description="dont click please")
            async def pingDerpy(interaction: discord.Interaction):
                await interaction.response.send_message("Crazy?")

            @bot.tree.command(name ="glaze", description="you wanna be glazed?")
            async def pingDerpy(interaction: discord.Interaction):
                global glazemode
                global glazeid
                glazeid = interaction.user.id
                if glazemode:
                    glazemode = False
                    await interaction.response.send_message("no more glaze for you")
                else:
                    glazemode = True
                    await interaction.response.send_message("Jarvis, activate glaze phase?")


            @bot.tree.command(name ="lobotomy", description="lobotomy 101")
            async def pingDerpy(interaction: discord.Interaction):
                await interaction.user.send("hi why do you want to give a lobotomy?")
                await interaction.user.send("hi why do you want to give a lobotomy?")
                await interaction.user.send("hi why do you want to give a lobotomy?")
                await interaction.user.send("hi why do you want to give a lobotomy?")
                await interaction.user.send("hi why do you want to give a lobotomy?")
                await interaction.user.send("hi why do you want to give a lobotomy?")
                await interaction.user.send("hi why do you want to give a lobotomy?")
                await interaction.user.send("hi why do you want to give a lobotomy?")
                await interaction.user.send("hi why do you want to give a lobotomy?")
                await interaction.user.send("hi why do you want to give a lobotomy?")
                await interaction.user.send("hi why do you want to give a lobotomy?")
                await interaction.user.send("hi why do you want to give a lobotomy?")
                await interaction.user.send("hi why do you want to give a lobotomy?")
                await interaction.user.send("hi why do you want to give a lobotomy?")
                await interaction.user.send("hi why do you want to give a lobotomy?")
                await interaction.user.send("hi why do you want to give a lobotomy?")


            @bot.tree.command(name ="pingyoself", description="pings")
            async def pingyoself(interaction: discord.Interaction, times: int):
                await interaction.response.send_message(f"<@{interaction.user.id}>")
                sutnh: bool = False
                if times >= 25:
                    sutnh = True
                    await interaction.response.send_message("ok im not gonna let you do this although it would be funny this is gonna go on forever")
                
                elif times > 1 and not sutnh:
                    
                    for x in range(times - 1):
                        
                        await interaction.channel.send(f"<@{interaction.user.id}>")
                
                elif times == 1:
                    await interaction.response.send_message(f"<@{interaction.user.id}>")
                
                elif times <= 0:
                    await interaction.response.send_message(f"syou fricking thug who do you think you are putting less than one on this thing i hate people like you. People like you shouldn't be allowed to use things like this its so horrible i hate you so much")


            @bot.tree.command(name ="pleasedontpress", description="uh oh")
            async def pleasedonotpress(interaction: discord.Interaction, times: int):
                if not times <= 0:
                    for x in range(times * 5):
                        await interaction.user.send("dumbass clanker i told you not to click this you dumbass no inteligent person?")


            @bot.tree.command(name ="ohnodontclick", description="ashtysdf ssdbfsdfas f")
            async def spamping(interaction: discord.Interaction, user : discord.Member, times: int):
                if not times <= 0 :
                    if times >= 25:
                        await interaction.response.send_message("gng how do you think they would feel if someone did this to you :sob: :wilted_rose: :low_battery:")
                    else:
                        for x in range(times):
                            await interaction.channel.send(f"<@{int(user.id)}>")
                            



        
        async def on_ready(self):
            global bot_testing_channel
            bot_testing_channel = bot.get_channel(bot_testing_channel_id)
            
            print(f"connected to server as {self.user}!!!!!!!!!!!!!!!")
            
            try:
                synced = await self.tree.sync(guild=GUILD_ID)
                glob_sync = await self.tree.sync()
                # you can add more specific server id's
                print(f"Synced {len(synced)} of my commands and {len(glob_sync)} globally")
            except Exception as e:
                print(f"Failed to sync commands: {e}")

        async def on_message(self, message):
            #if message.author == client.user:
            #    return
            
            print(f"{message.author} : {message.content}")

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
                    picture = discord.File("Derpybot\Fortnight.gif")
                    await message.channel.send(file = picture)

                case "School bathroom":
                    picture = discord.File("Derpybot/ThousandYardStare.png")
                    await message.channel.send(file = picture)
                
                case "School":
                    picture = discord.File("Derpybot/ThousandYardStare.png")
                    await message.channel.send(file = picture)
                
                case "boys bathroom":
                    picture = discord.File("Derpybot/ThousandYardStare.png")
                    await message.channel.send(file = picture)
                
                case "shutdown":
                    
                    await message.channel.send("gng ts does not work point and laugh, point and laugh")






intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = Client(command_prefix="!", intents=intents)

bot.run(magicTOKEN)

