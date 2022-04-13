# DiscordResponderBot
A simple Discord responder bot that will tell dad jokes, an inspirational quote, or just say hello.


(Hosted on free Heroku account. Will take a few seconds to "wake up" if it hasn't been accessed in the last 30 minutes.)

[Join my test server to give the bot a test drive!](https://discord.gg/s3THRWAVGM)

**Commands(must be at the beginning of a message):**

!bothelp - will explain the commands (not a slashcommand, just looks like one)

!dad joke - tells a random dad joke

!inspire - posts a random inspirational quote attributed to the author

!hello - responds with a random greeting

!kanye - responds with a random Kaybe quote

!roll - rolls a 6 sided die

!random - asks user for a number, returns a random number between 1 and that number

!satoshi - responds with current BTC spot price and satoshi cost of 2cents USD

!compliment - pays you a lovely (ok, they're mostly weird) compliment

!bingo - print a randomized bindo card


**To create a bot for your discord:**
1. Ensure you have admin permissions on the server you want to add your new bot to
2. Log in to discord website https://discord.com/
3. Go to Applications https://discord.com/developers/applications
4. Click "New Application"
5. Name your app, click "Create"
6. In sidebar, click "Bot" > "Add Bot" > "Yes, do it!"
7. Give your bot a username (can be same or different as the app name)
8. Copy the bot's TOKEN (you will use this in your code)
9. Go to "OAuth2" > "URL Generator"
10. Select "bot" in "SCOPES"
11. Give your bot the following permissions: (Read Messages/View Channels, Send Messages, Send Messages in Threads)
12. Copy the GENERATED URL and paste into your browser, this will invite your bot to the server you select
13. Check that your bot is in your server

**To use the main.py code**

**Replit**
1. Sign in/Register for Replit https://replit.com
2. Create a new repl > use python > call it anything you like > "Create Repl"
3. In main.py, copy the code of my main.py, or delete the file in Replit and upload mine
4. Go to "Secrets" (The lock on the left sidebar)
5. The key is TOKEN and the value is the bot's token you copied earlier > "Add New Secret"
6. Hit Run! As long as the program is running, the bot will operate.
