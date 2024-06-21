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

	if message.author == client.user:
		with open('output.txt', 'a') as f:
			f.write(f"{username} : {user_message}\n")
			print(f"{username} : {user_message}")
		return


	with open('output.txt', 'a') as f:
		f.write(f"{username} : {user_message}\n")
		print(f"{username} : {user_message}")

	await send_message(message, user_message)

def main() -> None:
	client.run(token=TOKEN)

if __name__ == '__main__':
	main()
