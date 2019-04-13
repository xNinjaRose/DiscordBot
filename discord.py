
#!/usr/bin/python3.6
import discord
from discord.ext import commands
from discord.ext.commands import Bot


#Discord Bots Auth Token
TOKEN = ("")

#tell the bot what key to start commands with
client = commands.Bot(command_prefix = '.')

#tell the console bot is ready


@client.event
async def on_ready():
    print ("bot is ready")
    print("Logged in as")

@client.event
async def on_message(message):
    #stops bot from replying to itself
    if message.author == client.user:
        return

    author = message.author
    content = message.content
    print("{}: {}".format(author, content))


    channel = message.channel
    if message.content.startswith('ping()'):
        await channel.send("Pong!")

    if message.content.startswith("echo()"):
        msg = message.content.split()
        output = ''
        for word in msg[1:]:
            output += word
            output += ' '
        await channel.send(output)

    if message.content.startswith("echo()"):
        msg = message.content.split()
        output = ''
        for word in msg[1:]:
            output += word
            output += ' '
        await channel.send(output)

    if message.content.startswith("hello()"):
        msg = "Hello {0.author.mention}".format(message)
        await channel.send(msg)


@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await channel.send("Deleted: {} {}".format(author,content))


#start the bot
client.run(TOKEN)
