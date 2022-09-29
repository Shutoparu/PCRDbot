import discord
from discord.ext import commands
import json
import os

with open('config.json', 'r', encoding='utf-8') as jconfig:
    config = json.load(jconfig)

#set bot access to different categories
intents = discord.Intents.all()


#the token to call the bot
bot = commands.Bot(command_prefix = config['PREFIX'], intents = intents)

#message sent when bot is online
@bot.event
async def on_ready():
    guild = bot.get_guild(eval(config['GUILD']))
    sign_up_channel = guild.get_channel(eval(config["報名"]))
    sl_channel = guild.get_channel(eval(config["閃退"]))
    lobby_channel = guild.get_channel(eval(config['LOBBY']))

    slRole = guild.get_role(eval(config['slUsed']))
    for member in slRole.members:
        await member.remove_roles(slRole)
    
    for i in range(1,6):
        bossRole = guild.get_role(eval(config[f'beatB{i}']))
        for member in bossRole.members:
            await member.remove_roles(bossRole)

    sign_up_messages = await sign_up_channel.history().flatten()
    await sign_up_channel.delete_messages(sign_up_messages)

    sl_messages = await sl_channel.history().flatten()
    await sl_channel.delete_messages(sl_messages)

    await sign_up_channel.send(config["報名資訊"])
    await sl_channel.send(config["閃退資訊"])
    await lobby_channel.send(config["ONLINE"])
    print('>bot online<')
    

#load commands and events
for commandFiles in os.listdir(path='./function'):
    if commandFiles.endswith('.py'):
        bot.load_extension(f'function.{commandFiles[:-3]}')

#manually load/unload/reload extension
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'function.{extension}')
    await ctx.send(f'{extension} load')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'function.{extension}')
    await ctx.send(f'{extension} unload')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'function.{extension}')
    await ctx.send(f'{extension} reload')


if __name__ == "__main__":
    bot.run(config['BOT_TOKEN'])

