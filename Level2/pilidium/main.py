from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response


# Loading our token...

load_dotenv()
TOKEN : Final[str] = os.getenv('DISCORD_TOKEN')


# Setting our bot up...

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


# Bot responding...

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := ('Vocare!' in user_message):
        user_message = 'private_default'

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# Handling the startup...

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# Handling incoming messages...

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# Entry...

def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()