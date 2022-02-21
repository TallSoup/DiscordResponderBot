import os
import discord
import random
import requests
from prettytable import PrettyTable

# set up gateway intents to pull member info below
intents = discord.Intents.default()
# intents.messages = True

# create connection to discord

client = discord.Client(intents=intents)


def quote():
    """returns a formatted inspirational quote with author"""
    response = requests.get("https://zenquotes.io/api/random").json()
    formatted_quote = f"{response[0]['q']} -{response[0]['a']}"
    return formatted_quote


def dad_joke():
    """returns a formatted dad joke"""
    headers = {"Accept": "application/json"}
    response = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    formatted_dad_joke = response['joke']
    return formatted_dad_joke


def kanye():
    """returns a formatted kanye quote with a random nickname"""
    kanye_names = ['Pablo', 'Yeezy', 'Yeezus', 'Ye', 'Mr.West',
                   'Kan The Louis Vuitton Don (Kanye - Better Than Yours)', 'The Don (Video)',
                   'Martin Louis the King, Jr. (Video)', 'KanYeezy (Jay-Z - Lucifer)',
                   'The LeBron of Rhyme (Kanye - DIAND)', 'K - Rock (Kanye - Drive Slow)',
                   "Omari/'Mari (Kanye - Only One)", 'The Black Zac Efron (Kenny West on the Cleveland Show)',
                   'Evel Kanyevel (Kanye - Touch the Sky video)', 'Swag King Cole (Kanye - Cold)']
    response = requests.get("https://api.kanye.rest")
    formatted_kanye_quote = f"{response.json()['quote']}  -{random.choice(kanye_names)}"
    return formatted_kanye_quote


def dice_roll():
    """rolls a 6 sided die, returns result"""
    roll = random.randint(1, 6)
    result = f"I rolled a 6 sided die and it landed on {roll}."
    return result


def random_picker(number):
    """returns a random selection between 1 and the number passed to it"""
    random_number = random.randint(1, int(number))
    return random_number


def satoshi():
    """returns a formatted message informign the value of 2 cents in satoshi"""
    response = requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD")
    btc_spot = response.json()['data']['amount']
    btc_spot = float(btc_spot)
    satoshi = btc_spot / 100000000
    two_cents = int(round(0.02 / satoshi, 0))
    # print(satoshi)
    # print(btc_spot)
    # print(two_cents)
    message = f"The current BTC spot price is ${btc_spot} (Source: coinbase.com).\nYour two cents = {two_cents} satoshis."
    # print(message)
    return message


def compliment():
    """pays you a weird compliment"""
    response = requests.get("https://complimentr.com/api")
    nice_words = response.json()['compliment'].capitalize()
    print(nice_words)
    return nice_words


def bingo():
    """returns a randomized bingo card"""
    table = PrettyTable()

    # create numbers for letters
    b = [x for x in range(1, 16)]
    i = [x for x in range(16, 31)]
    n = [x for x in range(31, 46)]
    g = [x for x in range(46, 61)]
    o = [x for x in range(61, 76)]

    # pull numbers for card
    b_list = []
    while len(b_list) < 5:
        x = random.choice(b)
        if x not in b_list:
            b_list.append(x)

    i_list = []
    while len(i_list) < 5:
        x = random.choice(i)
        if x not in i_list:
            i_list.append(x)

    n_list = []
    while len(n_list) < 5:
        x = random.choice(n)
        if len(n_list) == 2:
            n_list.append("FREE")
        if x not in n_list:
            n_list.append(x)

    g_list = []
    while len(g_list) < 5:
        x = random.choice(g)
        if x not in g_list:
            g_list.append(x)

    o_list = []
    while len(o_list) < 5:
        x = random.choice(o)
        if x not in o_list:
            o_list.append(x)

    # print(b)
    # print(i)
    # print(n)
    # print(g)
    # print(o)

    # create card

    # table.field_names = ["B", "I" , "N", "G", "O"]
    table.add_column("B", b_list)
    table.add_column("I", i_list)
    table.add_column("N", n_list)
    table.add_column("G", g_list)
    table.add_column("O", o_list)

    return f"``` {table} ```"


# list of greetings in reply to hello function
replies = ["Hi!", "Hello!", "How are you?", "Greetings!", "Good day to you", "Hallo!", "Hola!", "Bonjour", "Hey!"]


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    for guild in client.guilds:
        print(guild)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Greeting
    if message.content.lower().startswith('!hello'):
        await message.channel.send(random.choice(replies))

    # Inspiration
    if message.content.lower().startswith("!inspire"):
        await message.channel.send(quote())

    # Dad Joke
    if message.content.lower().startswith("!dad joke"):
        await message.channel.send(dad_joke())

    # Help Function
    if message.content.lower().startswith("!bothelp"):
        await message.channel.send(
            f"Use the following commands to control **{str(client.user).split('#')[0]}**: \n\n'hello' will respond with a random greeting \n'inspire' will respond with a"
            " random inspirational quote \n'dad joke' will tell you a random dad joke \n'kanye' will respond with a"
            "random Kanye West quote \n'roll' will roll a 6 sided die \n'random' will ask you for a number and "
            "return a number between 1 and the number you give it.\n'!satoshi' will tell you todays BTC spot price and "
            "the satoshi cost of your 2 cents USD.\n'!compliment' - pays you a lovely (ok, they're mostly weird) compliment\n"
            "'!bingo' will print a random bingo card.")

    # Kanye Quote
    if message.content.lower().startswith("!kanye"):
        await message.channel.send(kanye())

    # Dice Roll
    if message.content.lower().startswith("!roll"):
        await message.channel.send(dice_roll())

    # Random Number Chooser
    if message.content.lower().startswith("!random".lower()):
        author = message.author
        # channel = message.channel
        await message.channel.send("I'll pick a number, what is the highest number you want?")
        # wait for user response, then call function
        msg = await client.wait_for('message', check=lambda message: message.author == author)
        try:
            if int(msg.content) > 0:
                result = random_picker(msg.content)
                await message.channel.send(
                    f"I've randomly picked a number between 1 and {msg.content} and it is **{result}**.")
            else:
                await message.channel.send(f"{msg.content} is not valid, try again with a number greater than 0.")
        except ValueError:
            await message.channel.send(f"{msg.content} is not valid, try again with a number greater than 0.")

    # Satoshi
    if message.content.lower().startswith("!satoshi"):
        await message.channel.send(satoshi())

    # Compliment
    if message.content.lower().startswith("!compliment"):
        await message.channel.send(compliment())

    # Compliment
    if message.content.lower().startswith("!bingo"):
        await message.channel.send(bingo())


# In order for this to work, you'll need your bots token (keep this a secret, call with your preferred method, see readme for direction)
client.run(os.environ['TOKEN'])
