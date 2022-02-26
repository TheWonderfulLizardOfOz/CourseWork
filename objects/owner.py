from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Only runs if user is owner and loads cog
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, arg):
        try:
            self.bot.load_extension(arg)
        except Exception as e:
            await ctx.send("**`Error failed to load cog`**")
        else:
            await ctx.send("**`Successfully loaded cog`**")

    #Only runs if user is owner and unloads cog meaning that it's commands can't be accessed via discord
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, arg):
        try:
            self.bot.unload_extension(arg)
        except:
            await ctx.send("**`Error failed to unload cog`**")
        else:
            await ctx.send("**`Successfully unloaded cog`**")

    #Only runs if user is owner and is user to reload a cog which is used to quickly update without having to restart
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, arg):
        try:
            self.bot.unload_extension(arg)
            self.bot.load_extension(arg)
        except:
            await ctx.send(f"**`Error failed to relaod cof`**")
        else:
            await ctx.send("**`Successfully reloaded cog`**")

def setup(bot):
    bot.add_cog(Owner(bot))