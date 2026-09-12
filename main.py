import disnake #Вставити в main.py файл для регістраціїї команди
from disnake.ext import commands 

from BANNED_FILES.config import TOKEN

intents = disnake.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)



bot.load_extension("commands.host_cog") #Вставити в main.py файл для регістраціїї команди


@bot.event
async def on_ready():
    print(f"Бот запущен как {bot.user}")


if __name__ == "__main__":
    bot.run(TOKEN)