from random import choice, randint
import ollama

def get_response(user_input: str) -> str:
	lowered: str = user_input.lower()

	if lowered == '':
		return "uhhh rip.."
	elif 'becker' in lowered:
		return 'le beckre'
	elif 'keker' in lowered:
		return "ok sai"
	elif lowered[0] == "!":
		ai_response = ollama.chat(model='uncensored', messages=[
		  {
		    'role': 'user',
		    'content': lowered,
		  },
		])
		return str(ai_response['message']['content'])

	else:
		return
