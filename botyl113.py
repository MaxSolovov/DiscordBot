import discord
import random
from discord.ext import commands

TOKEN = "NzA0NTk5OTk0NzY5ODY2NzUz.XqfgGg.JMNy2Yfr4OZOWwOhtxw-H5CiBDI"

bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print(f'{bot.user} подключен к Discord!')
    for guild in bot.guilds:
        print(
            f'{bot.user} подключились к чату:\n'
            f'{guild.name}(id: {guild.id})'
        )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "привет бот" in message.content.lower():
        await message.channel.send("И тебе привет, человек")
        await message.channel.send("Чем помочь?")

    #await message.channel.send("Спасибо за сообщение")
    await bot.process_commands(message)


@bot.command(name='rnd')
async def my_randint(ctx, min_int, max_int):
    num = random.randint(int(min_int), int(max_int))
    await ctx.send(num)


bot.run(TOKEN)