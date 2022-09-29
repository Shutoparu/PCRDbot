from discord.ext import commands
import json
from DiscordBot.cogExtension import CogExtension

with open('/Users/kinoko/Desktop/python/DiscordBot/config.json', 'r', encoding='utf-8') as jconfig:
        config = json.load(jconfig)
    
class Event(CogExtension):

    i=1

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.content == config["報名資訊"] and message.author == self.bot.user:
            for num in range(1,6):
                await message.add_reaction(config[f"b{num}"])
        elif message.content == config["閃退資訊"] and message.author == self.bot.user:
            await message.add_reaction(config['sl'])
            
        
        elif message.content.startswith('現在是 ') and message.author == self.bot.user:
            self.i = message.content[-2]
            guild = self.bot.get_guild(eval(config['GUILD']))
            nextMembers = guild.get_role(eval(config[f'beatB{self.i}'])).members
            for member in nextMembers:
                await message.channel.send(f'{member.mention} |')

        elif message.content.endswith('|') and message.author == self.bot.user:
            await message.add_reaction(config['in'])
            await message.add_reaction(config['out'])
            await message.add_reaction(config['last'])

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        guild = self.bot.get_guild(eval(config['GUILD']))

        if payload.channel_id == eval(config['PROGRESS']) and payload.user_id != self.bot.user.id:
            botlogChannel = guild.get_channel(eval(config['BOTLOG']))
            progressChannel = guild.get_channel(eval(config['PROGRESS']))
            messageToTag = await progressChannel.fetch_message(payload.message_id)
            personToTag = messageToTag.mentions[0].mention

            if str(payload.emoji) == config['out']:
                await botlogChannel.send(personToTag + ' 出')
            elif str(payload.emoji) == config['last']:
                await botlogChannel.send(personToTag + " 尾刀")
            elif str(payload.emoji) == config['in']:
                pass
                

        elif payload.channel_id == eval(config['報名']) and payload.user_id != self.bot.user.id:
            progressChannel = guild.get_channel(eval(config['PROGRESS']))
          
            if int(str(payload.emoji)[3]) == int(self.i):
                await progressChannel.send(payload.member.mention + " |")

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if ctx.message.content.startswith('//'):
            pass
        else:
            await ctx.send(error)
            await ctx.send(type(error))
        


def setup(bot):
    bot.add_cog(Event(bot))

