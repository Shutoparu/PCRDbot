from discord.ext import commands
from DiscordBot.cogExtension import CogExtension
import json

with open('/Users/kinoko/Desktop/python/DiscordBot/config.json', 'r', encoding='utf-8') as jconfig:
        config = json.load(jconfig)

class Member(CogExtension):

    @commands.command()
    async def r(self,ctx,dmg,note):
        guild = self.bot.get_guild(eval(config['GUILD']))
        lobbyChannel = guild.get_channel(eval(config["LOBBY"]))
        if ctx.channel != lobbyChannel:
            return
        progressChannel = guild.get_channel(eval(config["PROGRESS"]))
        async for message in progressChannel.history():
            if len(message.mentions) != 0 and message.mentions[0] == ctx.author:
                await message.edit(content = f'{ctx.author.mention} | **{dmg}** : {note}')
      

    @commands.command()
    async def tk(self,ctx):
        guild = self.bot.get_guild(eval(config['GUILD']))
        slChannel = guild.get_channel(eval(config["閃退"]))
        if ctx.channel != slChannel:
            return
        history = await slChannel.history().flatten()
        await slChannel.delete_messages(history)
        slUsed = guild.get_role(eval(config["slUsed"]))
        for member in slUsed.members:
            await member.remove_roles(slUsed)
        await slChannel.send(config['閃退資訊'])



        

def setup(bot):
    bot.add_cog(Member(bot))

