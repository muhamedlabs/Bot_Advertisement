import platform
import time

import discord
from discord.ext import commands

START_TIME = time.time()

EMBED_COLOR = 0xFF265C

HOST_NAME = "ServerMuhameda - Приватный VPS сервер"
HOST_LOCATION = "Где-то на этой планете земля"
HOST_IMAGE = "https://i.ibb.co/HDdmH3xS/image.png"
HOST_LINK = "https://server.muhamedlabs.pro"
DEVELOPER = "Андрей Мухамед (admirall_times)"


class HostInfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="host", description="Показать информацию о хостинге бота")
    async def host(self, ctx: commands.Context):
        uptime_seconds = int(time.time() - START_TIME)
        hours, remainder = divmod(uptime_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        library_name = type(self.bot).__module__.split(".")[0]
        library_version = __import__(library_name).__version__

        embed = discord.Embed(
            title="● Информация о хостинге и боте",
            url=HOST_LINK,
            description=(
                "> **Server Muhameda** — место, где ваши проекты работают 24/7. "
                "Хостинг для Discord-ботов, приложений и игровых сервисов с удобным "
                "управлением и стабильной инфраструктурой."
            ),
            color=EMBED_COLOR,
        )
        embed.add_field(
            name="• О хостинге",
            value=(
                f"**Хост:** {HOST_NAME}\n"
                f"**Локация:** {HOST_LOCATION}\n"
                f"**Аптайм:** `{hours}ч {minutes}м {seconds}с`\n"
                f"**Пинг:** `{round(self.bot.latency * 1000)} мс`\n"
                f"**Статус:** Стабильно работает\n"
                f"**Разработчик:** {DEVELOPER}"
            ),
            inline=False,
        )
        embed.add_field(
            name="• О боте",
            value=(
                f"**Название:** {self.bot.user.display_name}\n"
                f"**Библиотека:** {library_name} `{library_version}`\n"
                f"**Python:** `{platform.python_version()}`\n"
                f"**Серверов:** `{len(self.bot.guilds)}`\n"
                f"**Пользователей:** `{sum(g.member_count or 0 for g in self.bot.guilds)}`"
            ),
            inline=False,
        )
        embed.set_image(url=HOST_IMAGE)
        embed.set_footer(text="Спасибо, что выбрали наш хост!")

        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(HostInfo(bot))
    print("Ког HostInfo (команда /host) успешно загружен")