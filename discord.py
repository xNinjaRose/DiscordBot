#!/usr/bin/python3.6
import discord
import clr 
import os
import json
import random 
from discord.ext import commands 
from discord import FFmpegPCMAudio
from discord.utils import get
from discord.ext.commands import Bot, has_permissions, CheckFailure
import youtube_dl


#import lyricwikia

#Discord Bots Auth Token
TOKEN = ("NTY2Mzc2ODUzMjUwNzY4OTg2.XLEHzg.aYcpsoW62bo5XS_y66PGit7C4uM")

#tell the bot what key to start commands with
client = commands.Bot(command_prefix=".",status=discord.Status.idle, activity=discord.Game(name="Booting.."))

#tell the console bot is ready
@client.event
async def on_ready():
    print (clr.green("Bot is Ready"))
    print (clr.blue(f"Serving:{len(client.guilds)} guilds."))
    nep = (client.user.name)
    print(clr.green("Logged in as", nep))
    print ('-------------------------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Active!"))

@client.event
async def on_member_join(member):
    channel = client.get_channel(451806689243430913)
    guild=member.guild
    message = "Hello {}, Welcome to {} Discord Server, We hope you have an awesome stay in Radiant Garden, Be sure to check out the rules channel before posting! :tada: :purple_heart:".format(member.mention, guild.name)
    await channel.send(message)

@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    await voice.move_to(channel)
    await ctx.send(f"Joined {channel}")

# @client.command()
# async def leave(ctx):
#     server = ctx.message.author.voice.channel
#     await server.disconnect()

# @client.command()
# async def play(ctx,url):
#     server = ctx.message.server
#     voice_client = client.voice_clients(server)
#     player = await voice_client.create_ytdl_player(url)
#     players[server.id] = player
#     player.start()

#returns Pong from the bot
@client.command()
async def ping (ctx):
    await ctx.send(f"Pong! :ping_pong: {round(client.latency * 1000)}ms")

#Returns the bot's ping
@client.command()
async def pings(ctx):
    ping_ = client.latency
    pings = round(ping_ * 1000)
    await ctx.channel.send(f"My ping is {pings}ms")

#Returns User stats for the server
@client.command()
async def user(ctx, member:discord.Member =None):
    if member == None:
        member = ctx.message.author
        pronoun = "Your"
    else:
        pronoun = "Their"
    name = f"{member.name}#{member.discriminator}"
    status = member.status
    joined = member.joined_at
    role = member.top_role 
    activity = member.activity 
    await ctx.channel.send(f"{pronoun} name is {name}, {pronoun} status is {status}, They joined at {joined}, {pronoun} rank is {role} and they are playing {activity}")

@client.command()
async def torchrng(ctx):
    torch_diff = ["Normal","Hard","Very Hard"]
    num_lifes = ["Hardcore","Non-Hardcore"]
    torch_class = ["Destroyer","Vanquisher","Alchemist","Airbender","Assassin","Barbarian","Demonologist","Enchanter",
                "Executioner","Fomar","Fury","Gunblade","Guardian","Ice Queen","Lady Knight","Nethermage","Paladin","Shaman",
                "Sorceress","Spiritdancer","Stone Brother","Valkyrie","Warmage","Warlock"]
    
    await ctx.send(f"Your run will be {random.choice(torch_class)} on {random.choice(torch_diff)} with {random.choice(num_lifes)} enabled")

@client.command()
async def tq(ctx,answera):
    if answera == "none":
        masterynon = ["Warfare","Defense","Rune","Hunting"]
        await ctx.send(f"Your build will be {random.choice(masterynon)} and {random.choice(masterynon)}")
    elif answera == "all":
        masteryall = ["Earth","Storm","Dream","Warfare","Spirit","Defense","Nature","Rune","Hunting","Rogue"]
        await ctx.send(f"Your build will be {random.choice(masteryall)} and {random.choice(masteryall)}")

@client.command()
async def whois (ctx,gearname):
    
    dmgear = ["VladofSniper","EtechSniper","DahlSniper","HyperionShotgun","JakobsShotgun","TedioreShotgun","HyperionSmg",
    "DahlSmg","BanditSmg","TediorePistol","MaliwanPistol","EtechPistol","VladofPistol","TorguePistol","DahlGrenade","MaliwanGrenade",
    "BanditGrenade","PangolinShield","VladofShield","HyperionShield","DahlShield","VladofRpg","BanditRpg","TorgueRpg","JakobsAR",
    "VladofAR","EtechAR"]

    if gearname in dmgear:
        await ctx.send("That is DMMD's piece of gear! :dog: Hands off!!")
    else: 
        await ctx.send("That is Neko's piece of gear! :cat: Hands off!!")


@client.command()
async def roll(ctx):
    rollvar = ["Neko Wins The Round","DMMD Wins The Round"]
    await ctx.send(f"Result: {random.choice(rollvar)}")

@client.command()
async def ask(ctx, *, question):
    responses = json.loads(open('responses.json').read())
   # for response in responses:
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


####################################################################################
#BANS A USER WITH A REASON#
@client.command()
@commands.has_any_role("Keyblade Master","Foretellers")
async def ban (ctx, member:discord.User=None, reason =None):
    
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot ban yourself")
            return
        
        elif reason == None:
            reason = "being a jerk!"
            
        message = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(message)
        # await ctx.guild.ban(member)
        await ctx.channel.send(f"{member} is banned!") 

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("You do not have permission to do that!")
    else:
        raise error
###################################################################################     


@client.command()
async def nepscore(ctx):
    embed = discord.Embed(title="NepFul PermaDeath Challenge",description="Current Running Scores for the challenge",colour=discord.Color.purple(),url="https://docs.google.com/spreadsheets/d/1teWSgV56tdSj8jbgE6nNeDOGBm4ZUYluJ9Yi7ANZ0JE")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://images2.alphacoders.com/480/thumb-1920-480538.png")
    embed.set_thumbnail(url="https://pngimage.net/wp-content/uploads/2018/06/neptunia-png-4.png")
    await ctx.send(embed=embed)

@client.command()
async def dmmd(ctx):
    embed = discord.Embed(title="DMMD's Twitch Stream",description="Watch Pure Vanilla 1 Life Runs with Gaige and Zer0 here!",colour=discord.Color.purple(),url="https://www.twitch.tv/diemarlboromandie")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://images2.alphacoders.com/480/thumb-1920-480538.png")
    embed.set_thumbnail(url="https://pngimage.net/wp-content/uploads/2018/06/neptunia-png-4.png")
    await ctx.send(embed=embed)

##########################################################################################
#PURGES MESSAGES IN CHANNELS .PURGE 20 - 20 LINES ABOVE INCLUDING THAT LINE
@client.command()
@commands.has_any_role("Keyblade Master","Foretellers")
async def purge(ctx, amount: int):
    deleted = await ctx.channel.purge(limit = amount)
    await ctx.send(f"Deleted {len(deleted)} messages")

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.channel.send("Looks like you don't have permission for that!")
##########################################################################################

@client.command()
async def dmmdbl2(ctx):
    embed = discord.Embed(title="Borderlands 2 Personal Bests",description="The Personal Best Permadeath Stats")
    embed.add_field(name="Zer0",value="Lv 36 : TVHM, Dead to suicide psycho in Bloodshot")
    embed.add_field(name="Gaige", value ="Lv 37 : Dead at Ser Snowflake Boss off the edge")
    embed.add_field(name="Best 5 Game Aggregate", value ="121")
    embed.set_thumbnail(url="http://img3.wikia.nocookie.net/__cb20130922041206/borderlands/images/c/ce/BL2-Gaige-Head-Pithy_Rejoinder.png")
    await ctx.channel.send(embed=embed)

@client.command()
async def dmmdtq(ctx):
    embed = discord.Embed(title="TitanQuest Personal Best",description="The Personal Best Permadeath Stats")
    embed.add_field(name="Best Permadeath",value="Level 37 Berserker Post-Shade Feaster")
    embed.set_thumbnail(url="https://store-images.s-microsoft.com/image/apps.4301.13510798887926315.4daba2a4-159c-4d0a-9f90-d1c6f64c550d.0669b37a-aa6f-451d-b2d8-8752b9736d42")
    await ctx.channel.send(embed=embed)

# @client.command()
# async def lyrics(ctx,artist,title):
#     lyrics = lyricwikia.get_lyrics(artist,title)
#     await ctx.channel.send(lyrics)



@client.event
async def on_message(message):
    #stops bot from replying to itself
    if message.author == client.user:
        return

    author = message.author
    content = message.content 
    print("{}: {}".format(author, content))

    #GreetingList = ["hello","hi","Hey","Yo","yo","hey","Hello"]

    #blacklist_words = ["bad","politics","Clinton"]
    greetings = json.loads(open('greetings.json').read())
    swears = json.loads(open('badwords.json').read())

    for greet in greetings:
        if message.content.count(greet) > 0:
            await message.channel.send("Hello {0.author.mention}!".format(message))


    for word in swears:
        if message.content.count(word) > 0:
            print ("A Blacklisted Word was said")
            await message.channel.purge(limit=1)
            await message.channel.send("**Don't say bad words! Keep this chat family friendly.**")
    
    # if message.content == "!lyrics":

    #     messg = ' '.join(message.content.split(' ')[1:])
    #     artist = messg.split('+')[0]
    #     song = messg.split('+'[1])
    #     print(artist, song)
    #     lyrics = lyricwikia.get_lyrics(artist,song)
    #     embed = discord.Embed(title="Lyrics of {}".format(song.upper()),description = lyrics,color=discord.Color.dark_purple())
    #     await message.channel.send(embed=embed)


    if message.content == "help()":
        embed = discord.Embed(title="NepBot Help",description="Commands that NepBot knows")
        embed.add_field(name=".pings",value="Checks the latency of the bot")
        embed.add_field(name="!users", value ="Prints the number of users")
        embed.add_field(name=".user", value ="Shows user stats")
        embed.add_field(name=".ban", value ="Bans a user(only super mods)")
        embed.add_field(name="!tq", value ="Either All or None to randomize your TQ build")
        embed.add_field(name=".nepscore", value ="Shows NepFul PermaDeath Challenge Scores")
        embed.add_field(name=".dmmd", value ="Shouts out DMMD's twitch stream")
        embed.add_field(name=".purge", value ="Purge a # of lines(SuperMod only)")
        embed.add_field(name=".dmmdbl2", value ="Shows DMMDs Personal Bests")
        embed.add_field(name=".dmmdtq", value ="Shows DMMDs Personal Bests")
        embed.add_field(name="!ping", value ="Fun command, TRY IT! :D")
        embed.add_field(name="!echo", value ="have the bot echo what you want to say")
        await message.channel.send(embed=embed)

    # if message.content.find("hey") != -1:
    #     await message.channel.send("Hello {0.author.mention}".format(message))

    if message.content == "!users":
        id_a = client.get_guild(451803195488862208)
        await message.channel.send(f"Number of Members: {id_a.member_count}")

    if message.content.startswith("!echo"):
        msg = message.content.split()
        output = ''
        for word in msg[1:]:
            output += word
            output += ' '
        await channel.send(output)
 
      
    await client.process_commands(message)

@client.event
async def on_message_delete(message):
    author = message.author
    #content = message.content 
    channel = message.channel
    await channel.send("Deleted: Message From {} ".format(author))
    # await channel.send_message(channel,"{}: {}".format(author, content))

#start the bot
client.run(TOKEN)
