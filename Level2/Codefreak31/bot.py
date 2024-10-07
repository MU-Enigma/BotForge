import os
import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up the bot with a command prefix and intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Spotify API setup
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

if SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET:
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                               client_secret=SPOTIFY_CLIENT_SECRET))
else:
    raise ValueError("Spotify credentials not set properly in Replit secrets.")

# Event when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

# Command for music recommendations based on artist
@bot.command()
async def recommend(ctx, artist: str = None):
    """Recommend top 5 songs based on an artist."""
    if artist is None:
        await ctx.send("Please provide an artist name. Example: !recommend Adele")
        return
    
    try:
        # Search for top 5 songs by the provided artist
        results = sp.search(q=f'artist:{artist}', type='track', limit=5)

        if results['tracks']['items']:
            # Prepare a message with top 5 songs
            songs_message = f"🎶 **Top 5 songs by {artist}:**\n"
            for idx, track in enumerate(results['tracks']['items'], 1):
                track_name = track['name']
                artist_name = track['artists'][0]['name']
                track_url = track['external_urls']['spotify']
                songs_message += f"{idx}. **{track_name}** by **{artist_name}**\nListen here: {track_url}\n\n"
            
            await ctx.send(songs_message)
        else:
            await ctx.send(f"Sorry, I couldn't find any songs by '{artist}'.")

    except Exception as e:
        await ctx.send(f"An error occurred while fetching recommendations: {str(e)}")

# Run the bot
TOKEN = os.getenv('DISCORD_TOKEN')  # Ensure this environment variable is set in Replit
if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: DISCORD_TOKEN is not set. Please set it in the Replit environment variables.")
