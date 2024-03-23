import discord
from discord.ext import commands
from discord import app_commands


class maps(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(
        name="maps", description="produces a map based on what location you ask for!"
    )
    async def maps(self, interaction: discord.Interaction):
        # add connection to the database for name of the map location and the map image.
        # then display the map to the server
        # extension add some ability to find the closest location name.
        # ie, "Movarea" should recommend "Movaria" map as the closest match
        await interaction.response.send_message(content="Here is your map!")


async def setup(client: commands.Bot) -> None:
    await client.add_cog(maps(client))
