import os
import discord
import random
import requests


def quote():
    """returns a formatted quote with author"""
    response = requests.get("https://zenquotes.io/api/random").json()
    formatted_quote = f"{response[0]['q']} -{response[0]['a']}"
    return formatted_quote


def dad_joke():
    """returns a formatted dad joke"""
    headers = {"Accept": "application/json"}
    response = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    formatted_dad_joke = response['joke']
    return formatted_dad_joke


# list of greetings in reply to hello function
replies = ["Hi!", "Hello!", "How are you?", "Greetings!", "Good day to you", "Hallo!", "Hola!", "Bonjour", "Hey!"]


client = discord.Client()


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Greeting
    if message.content.startswith('hello'):
        await message.channel.send(random.choice(replies))

    # Inspiration
    if message.content.startswith("inspire"):
        await message.channel.send(quote())

    # Dad Joke
    if message.content.startswith("dad joke"):
        await message.channel.send(dad_joke())

    # Help Function
    if message.content.startswith("/bothelp"):
        await message.channel.send(
            "Use the following commands: 'hello' will respond with a random greeting, 'inspire' will respond with a random insirational quote, and 'dad joke' will tell you a random dad joke.")


# In order for this to work, you'll need your bots token (keep this a secret, call with your preferred method, see readme for direction)
client.run(os.environ['TOKEN'])
