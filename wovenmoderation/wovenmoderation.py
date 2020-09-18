from redbot.core import commands


class WovenModeration(commands.Cog):
    """
    Planned features:
    Replace Carl-bot's moderation features with our own, allowing for better customization.
    """
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
