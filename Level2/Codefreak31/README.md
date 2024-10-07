This bot functionality is designed to recommend music based on the artist you choose from Spotify.
Required Libraries

You will need to install the following libraries:

    discord.py: To build the Discord bot.
    spotipy: To interact with the Spotify API for music recommendations.
    requests: For making HTTP requests (optional).
    python-dotenv: To manage environment variables (optional).

You can install these libraries by running the following command:

bash

pip install discord.py spotipy requests python-dotenv

Programming Language and Environment

The code is written in Python and developed on Replit.
API Requirements

You will need the following APIs:

    Discord API: Obtain the Bot Token, which enables interaction with the Discord platform.
    Spotify API:
        Client ID: For accessing music recommendations.
        Client Secret: For user authentication, which is unique to each user.

Creating a Discord Server

    Click on Add New Server in Discord.
    Select Create My Own and choose For Me and My Friends.
    Enter a name for your server and click Create.

Obtaining the Bot Token

    Go to the Discord Developer Portal to create an application.
    Click on Create New Application and provide a name.
    Navigate to the Bot section in the left sidebar.
    Click on Reset Token; you will be prompted to enter your password for Multi-Factor Authentication (MFA).
    Copy the Token from there.
    Under Privileged Gateway Intents, enable the following:
        Message Content Intent
        Server Member Intent

Setting Up Bot Permissions

    In the Bot section, scroll down to Bot Permissions.
    Select the necessary permissions for your bot, such as:
        Send Messages
        Read Messages
        Embed Links
        Attach Files (if necessary)
        Read Message History
        Manage Messages (optional)
        Connect (if applicable)
        Speak (if applicable)
        Use External Emojis (if applicable)

Generating OAuth2 URL

    Go to the OAuth2 section in the left sidebar.
    In the Scopes section, select Bot.
    Under Bot Permissions, choose the necessary permissions for your bot.
    A generated URL will appear at the bottom. Copy this link and paste it into your browser to invite the bot to your Discord server.

Connecting Spotify to Discord and Getting Recommendations

    Go to Spotify Developer Dashboard.
    Log in to your existing Spotify Account and create a new app.
    After creating the app, you will see a Client ID and Client Secret; copy them.

Setting Up the Bot in Replit

    Create a new account or log in if you already have one on Replit, and create a new Repl.
    Go to Secrets and add the Discord Bot Token, Client ID of Spotify, and Client Secret of Spotify.
    Now that you're ready with everything, copy and paste the code provided in the .py file in this folder and click on Run.
    Once the code is successfully compiled, go to your Discord server and type !recommend <artist>. You will receive the top 5 tracks of that artist.

Usage Instructions

After setting up everything, you can start using the bot. Simply type !recommend <artist> in your Discord server. For example, you can try:

    !recommend Adele
    !recommend The Weeknd

The bot will then provide you with the top 5 tracks by the specified artist.

The code to be run every time when you are on the server because it is not deployed.


Troubleshooting

If you encounter issues, consider the following:

    Ensure that your API keys are correctly set in Replit's Secrets.
    Check that the bot has the necessary permissions in your Discord server.
    Verify that the bot is running and displaying the "Logged in as..." message in the console.