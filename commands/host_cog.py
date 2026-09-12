import platform
import time

import disnake
from disnake.ext import commands

START_TIME = time.time()

Embed_Color = "#ff265c"

HOST_NAME = "ServerMuhameda - Приватный VPS сервер"
HOST_LOCATION = "Где-то на этой планете земля"
HOST_IMAGE = "https://i.ibb.co/HDdmH3xS/image.png"
HOST_LINK = "https://server.muhamedlabs.pro"
BOT_DEVELOPER = "Андрей Мухамед (admirall_times)"


class HostInfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embed_color = disnake.Color(int(Embed_Color.lstrip("#"), 16))

    @commands.slash_command(name="host", description="Показать информацию о хостинге бота")
    async def host(self, inter: disnake.ApplicationCommandInteraction):
        uptime_seconds = int(time.time() - START_TIME)
        hours, remainder = divmod(uptime_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        library_name = type(self.bot).__module__.split(".")[0]
        library_version = __import__(library_name).__version__

        container = disnake.ui.Container(
            disnake.ui.TextDisplay("# ● Информация о хостинге и боте"),
            disnake.ui.TextDisplay(
                "> **Server Muhameda** — место, где ваши проекты работают 24/7. "
                "Хостинг для Discord-ботов, приложений и игровых сервисов с удобным "
                "управлением и стабильной инфраструктурой."
            ),
            disnake.ui.Separator(),
            disnake.ui.TextDisplay("## • Хостинг"),
            disnake.ui.TextDisplay(
                f"**Хост:** {HOST_NAME}\n"
                f"**Локация:** {HOST_LOCATION}\n"
                f"**Аптайм:** `{hours}ч {minutes}м {seconds}с`\n"
                f"**Пинг:** `{round(self.bot.latency * 1000)} мс`\n"
                f"**Статус:** Стабильно работает\n"
                f"**Разработчик:** {BOT_DEVELOPER}"
            ),
            disnake.ui.Separator(),
            disnake.ui.TextDisplay("## • Бот"),
            disnake.ui.TextDisplay(
                f"**Название:** {self.bot.user.display_name}\n"
                f"**Библиотека:** {library_name} `{library_version}`\n"
                f"**Python:** `{platform.python_version()}`\n"
                f"**Серверов:** `{len(self.bot.guilds)}`\n"
                f"**Пользователей:** `{sum(g.member_count or 0 for g in self.bot.guilds)}`"
            ),
            disnake.ui.MediaGallery(disnake.MediaGalleryItem(HOST_IMAGE)),
            disnake.ui.Separator(),
            disnake.ui.TextDisplay(
                f"-# Спасибо, что выбрали наш хост! [Перейти на сайт хостинга.]({HOST_LINK})"
            ),
            accent_colour=self.embed_color,
        )

        await inter.response.send_message(
            components=[container],
            flags=disnake.MessageFlags(is_components_v2=True),
        )


def setup(bot: commands.Bot):
    bot.add_cog(HostInfo(bot))
    print("Ког HostInfo (команда /host) успешно загружен")