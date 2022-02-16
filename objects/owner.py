from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Only runs if user is owner and loads cog
    @commands.command(name="load")
    @commands.is_owner()
    async def loadCog(self, ctx, arg):
        try:
            self.bot.load_extension(arg)
        except Exception as e:
            await ctx.send(f"**`Error`** {type(e).__name__} - {e}")
        else:
            await ctx.send("**`Success`**")

    #Only runs if user is owner and unloads cog meaning that it's commands can't be accessed via discord
    @commands.command(name = "unload")
    @commands.is_owner()
    async def unloadCog(self, ctx, arg):
        try:
            self.bot.unload_extension(arg)
        except Exception as e:
            await ctx.send(f"**`Error`** {type(e).__name__} - {e}")
        else:
            await ctx.send("**`Success`**")

    #Only runs if user is owner and is user to reload a cog which is used to quickly update without having to restart
    @commands.command(name = "reload")
    @commands.is_owner()
    async def reloadCog(self, ctx, arg):
        try:
            self.bot.unload_extension(arg)
            self.bot.load_extension(arg)
        except Exception as e:
            await ctx.send(f"**`Error`** {type(e).__name__} - {e}")
        else:
            await ctx.send("**`Success`**")

def setup(bot):
    bot.add_cog(Owner(bot))