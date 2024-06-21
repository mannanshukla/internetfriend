import os
import ollama

def get_response(user_input: str) -> str:
	lowered: str = user_input.lower()

	if lowered == '':
		return "uhhh rip.."
	elif lowered[0] == "!":
		with open("output.txt", 'r') as file:
			content = file.read()
		prompt = lowered[1:] + content 
		ai_response = ollama.chat(model='uncensored', messages=[
		  {
			'role': 'user',
			'content': prompt,
		  },
		])
		return str(ai_response['message']['content'])

	else:
		return
