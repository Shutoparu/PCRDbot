from discord.ext import commands
import json
from DiscordBot.cogExtension import CogExtension

with open('/Users/kinoko/Desktop/python/DiscordBot/config.json', 'r', encoding='utf-8') as jconfig:
        config = json.load(jconfig)

class Role(CogExtension):
    
    

    #add
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):

        #sign up
        if payload.channel_id == eval(config["報名"]) and payload.user_id != self.bot.user.id:
            for i in range(1,6):
                if str(payload.emoji) == config[f'b{i}']:
                    guild = self.bot.get_guild(payload.guild_id)
                    role = guild.get_role(eval(config[f'beatB{i}']))
                    await payload.member.add_roles(role)
        elif payload.channel_id == eval(config["閃退"]) and payload.user_id != self.bot.user.id:
            if str(payload.emoji) == config['sl']:
                guild = self.bot.get_guild(payload.guild_id)
                role = guild.get_role(eval(config['slUsed']))
                await payload.member.add_roles(role)
    
    #remove
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):

        if payload.channel_id == eval(config["報名"]) and payload.user_id != self.bot.user.id:
            for i in range(1,6):
                if str(payload.emoji) == config[f'b{i}']:
                    guild = self.bot.get_guild(payload.guild_id)
                    role = guild.get_role(eval(config[f'beatB{i}']))
                    user = guild.get_member(payload.user_id)
                    await user.remove_roles(role)
        elif payload.channel_id == eval(config["閃退"]) and payload.user_id != self.bot.user.id:
            if str(payload.emoji) == config['sl']:
                guild = self.bot.get_guild(payload.guild_id)
                role = guild.get_role(eval(config['slUsed']))
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)

def setup(bot):
    bot.add_cog(Role(bot))