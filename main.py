from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
import time

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:

    if not user_message:
        print('message empty')
        return

    try:
        response: str = get_response(user_message)
        chunks = []

        if len(response) >= 2000:
            for i in range(len(response)//2000 + 1):
                chunks.append(response[2000*i:2000+(2000*i)])
                await message.channel.send(chunks[i])
                
        else:
            await message.channel.send(response)
    
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print("bots running now..")

@client.event
async def on_message(message: Message) -> None:

    username: str = str(message.author)
    user_message: str = message.content
    lee: str = "lee cirelli becker"

    if message.author == client.user:
        with open('output.txt', 'a') as f:
            f.write(f"{username} : {user_message}\n")
            print(f"{username} : {user_message}")
        return


    with open('output.txt', 'a') as f:
        f.write(f"{username} : {user_message}\n")
        print(f"{username} : {user_message}")
    
    if user_message[0] == '!':
        await send_message(message, user_message)
    
    else:
        pass

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
