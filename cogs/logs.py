import discord
from discord.ext import commands
import os
import time
from .helpers import HelperFunctions


class Logs(commands.Cog, HelperFunctions):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    async def cog_check(self, ctx):
        return self.is_admin(ctx)

    # Commands
    @commands.command()
    async def logs(self, ctx, type="-info"):
        file_name = None
        if type == "-error":
            file_name = "/home/leaguebot/.pm2/logs/LeagueDiscordBot-error-0.log"
        elif type == "-std":
            file_name = "/home/leaguebot/.pm2/logs/LeagueDiscordBot-out-0.log"
        elif type == '-info':
            file_name = "/home/leaguebot/LeagueGameNotify/info.log"
        elif type == '-debug':
            file_name = "/home/leaguebot/LeagueGameNotify/debug.log"
        else:
            await ctx.send(f"Log file {type} not found. Please use -error, -std, -info or -debug")
            return

        t = time.ctime(os.path.getmtime(file_name))
        await ctx.send(f"Log file last updated on: {t}", file=discord.File(file_name))

# Connect cog to bot


def setup(bot):
    bot.add_cog(Logs(bot))
