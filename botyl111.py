import discord
import random
from discord.ext import commands

TOKEN = "NzA0NjU1MTc0NTk3MjE0MjQ4.XqgTVg.WHgbqdV1hG_SDfODOAGmL0K4Bcs"
# client = discord.Client()

bot = commands.Bot(command_prefix='!')

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

# class YLBotClient(discord.Client):
#     async def on_ready(self):
#         print(f'{self.user} has connected to Discord!')
#         for guild in self.guilds:
#             print(
#                 f'{self.user} подключились к чату:\n'
#                 f'{guild.name}(id: {guild.id})')
#
#     async def on_member_join(self, member):
#         await member.create_dm()
#         await member.dm_channel.send(
#             f'Привет, {member.name}!'
#         )
#
#     async def on_message(self, message):
#         if message.author == self.user:
#             return
#         if "привет бот" in message.content.lower():
#             await message.channel.send("И тебе привет, человек")
#             await message.channel.send("Чем помочь?")
#
#
#
#
# client = YLBotClient()
#
#
#
#client.run(TOKEN)

# dashes = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
#
#
# class RandomThings(commands.Cog):
#
#     def __init__(self, bot):
#         self.bot = bot
#
#     @commands.command(name='roll_dice')
#     async def roll_dice(self, ctx, count):
#         res = [random.choice(dashes) for _ in range(int(count))]
#         await ctx.send(" ".join(res))
#
#     @commands.command(name='randint')
#     async def my_randint(self, ctx, min_int, max_int):
#         num = random.randint(int(min_int), int(max_int))
#         await ctx.send(num)
#
#
# bot = commands.Bot(command_prefix='!#')
# bot.add_cog(RandomThings(bot))
# bot.run(TOKEN)



