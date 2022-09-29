from discord.ext import commands
from DiscordBot.cogExtension import CogExtension
import json

with open('/Users/kinoko/Desktop/python/DiscordBot/config.json', 'r', encoding='utf-8') as jconfig:
        config = json.load(jconfig)

class Boss(CogExtension):

    i=1
    j=1

    @commands.command()
    async def start(self,ctx):
        guild = self.bot.get_guild(eval(config['GUILD']))
        progressChannel = guild.get_channel(eval(config['PROGRESS']))
        if ctx.channel == progressChannel:
            if self.i != 1 or self.j != 1:
                return
            history = await progressChannel.history().flatten()
            await progressChannel.delete_messages(history)
            await ctx.send(config['周目資訊'].format(self.i,self.j))

    @commands.command()
    async def fin(self,ctx):
        guild = self.bot.get_guild(eval(config['GUILD']))
        progressChannel = guild.get_channel(eval(config['PROGRESS']))
        if ctx.channel == progressChannel:
            botlogChannel = guild.get_channel(eval(config['BOTLOG']))
            mentionAll = guild.get_role(eval(config["互肛"])).mention
            await botlogChannel.send(f'{mentionAll} {self.j}王已經倒了 請進下一個王')
            self.j+=1
            if self.j>=6:
                self.i+=1
                self.j=1
            history = await progressChannel.history().flatten()
            await progressChannel.delete_messages(history)
            await ctx.send(config['周目資訊'].format(self.i,self.j))
            mentionNext = guild.get_role(eval(config[f'beatB{self.j}'])).mention
            await botlogChannel.send(f'{mentionNext} 請進{self.j}王')

    @commands.command()
    async def restartBossCounter(self,ctx):
        guild = self.bot.get_guild(eval(config['GUILD']))
        progressChannel = guild.get_channel(eval(config['PROGRESS']))
        if ctx.channel == progressChannel:
            self.i=1
            self.j=1
            history = await progressChannel.history().flatten()
            await progressChannel.delete_messages(history)
            await ctx.send(config['周目資訊'].format(self.i,self.j))

    @commands.command()
    async def setBossCounter(self, ctx, num1,num2):
        guild = self.bot.get_guild(eval(config['GUILD']))
        progressChannel = guild.get_channel(eval(config['PROGRESS']))
        if ctx.channel == progressChannel:
            if int(num2) > 5 or int(num2) < 1:
                return
            self.i=int(num1)
            self.j=int(num2)
            history = await progressChannel.history().flatten()
            await progressChannel.delete_messages(history)
            await ctx.send(config['周目資訊'].format(self.i,self.j))
            

def setup(bot):
    bot.add_cog(Boss(bot))

