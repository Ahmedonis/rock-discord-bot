import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot_lost = [
    "You got lucky this time😒, human… enjoy it while it lasts!",
    "Okay, okay, you win… don’t get used to it!😤",
    "Hmm, impressive. But the Rock will be back!⛰️",
    "You got me… this isn’t over!",
    "Alright, you got one on me. I’ll let it slide… this time.🎚 get it slide..slider....ok sorry"
]

bot_lost_angry = [
    "Okay, you’re up 2 points…😤 Don’t get cocky!",
    "THIS IS UNACCEPTABLE!⛰️ I CAN’T BELIEVE THIS!😡",
    "HOW DARE YOU KEEP BEATING A ROCK?!🤬🔥",
    "ENOUGH! THE ROCK WILL CRUSH YOU!💪⛰️💥"
]

bot_won = [
    "Ha! The Rock crushes your move like a boulder!⛰️",
    "Too easy! The Rock reigns supreme!😎",
    "Your rock can’t stand against The Rock!😏",
    "Rocks may be just smarter than humans🤷‍♂️",
    "Feel that? That’s the power of The Rock!😎"
]

tie = [
    "It’s a tie! Looks like we’re evenly matched… for now.😒",
    "Stalemate! The Rock respects your skills… a little.😜",
    "We’re on the same wavelength! Try again!😂",
    "No winner this round… The Rock is intrigued.🙄",
    "A tie! Keep your eyes on The Rock, it’s about to get interesting.😏"
]


@bot.event
async def on_ready():
    print("The Rock has logged in")

choices = ["rock", "paper", "scissors"]
rps_dic = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}
bot_choice = None
player_points = {}
bot_points = {}
player_streak = {}
bot_loss_streak = 0
index = {}


@bot.command()
async def rps(ctx, player_choice):
    # global player_points, bot_points, player_streak, index  # , bot_loss_streak
    user_id = ctx.author.id

    if user_id not in player_points:
        player_points[user_id] = 0
        bot_points[user_id] = 0
        player_streak[user_id] = 0
        index[user_id] = 0

    bot_choice = random.choice(choices)
    player_choice = player_choice.lower()
    if player_choice not in ["rock", "paper", "scissors"]:
        await ctx.send('Only use "rock", "paper" or "scissors"')
    elif player_choice == bot_choice:
        # bot_loss_streak = 0
        await ctx.send(f"{ctx.author.mention} : {player_points[user_id]} | The Rock : {bot_points[user_id]}")
        await ctx.send(random.choice(tie))
    elif rps_dic[player_choice] == bot_choice and 0 <= player_streak[user_id] <= 1:
        player_streak[user_id] += 1
        player_points[user_id] += 1
        # bot_loss_streak += 1
        await ctx.send(f"{ctx.author.mention} : {player_points[user_id]} | The Rock : {bot_points[user_id]}")
        await ctx.send(random.choice(bot_lost))
    elif rps_dic[player_choice] == bot_choice and 2 <= (player_streak[user_id]) <= 5:
        player_streak[user_id] += 1
        player_points[user_id] += 1
        # bot_loss_streak += 1
        index[user_id] = min(player_streak[user_id] -
                             2, len(bot_lost_angry) - 1)
        angry_response = bot_lost_angry[index[user_id]]
        await ctx.send(f"{ctx.author.mention} : {player_points[user_id]} | The Rock : {bot_points[user_id]}")
        await ctx.send(angry_response)
    elif rps_dic[player_choice] == bot_choice and (player_streak[user_id]) == 6:
        player_streak[user_id] += 1
        player_points[user_id] += 1
        # bot_loss_streak += 1
        await ctx.send(f"{ctx.author.mention} : {player_points[user_id]} | The Rock : {bot_points[user_id]}")
        await ctx.send("You've got to be legendary, I admit..defeat.😵💨")
    else:
        # bot_loss_streak = 0
        player_streak[user_id] = 0
        bot_points[user_id] += 1
        await ctx.send(f"{ctx.author.mention} : {player_points[user_id]} | The Rock : {bot_points[user_id]}")
        await ctx.send(random.choice(bot_won))


@bot.command()
async def reset(ctx):
    # global player_points, bot_points, player_streak, index  # , bot_loss_streak
    user_id = ctx.author.id
    player_points[user_id] = 0
    player_streak[user_id] = 0
    bot_points[user_id] = 0
    index[user_id] = 0
    await ctx.send(f"{ctx.author.mention}, your game has been reset! 🎮")
    # bot_loss_streak = 0

bot.run(TOKEN)
