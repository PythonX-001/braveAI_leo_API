import requests
import aiohttp
from .models import LeoCompleteResponse

class Leo:
    def __init__(self, brave_key = 'qztbjzBqJueQZLFkwTTJrieu8Vw3789u', base_url = 'https://ai-chat.bsg.brave.com'):
        self.brave_key = brave_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'x-brave-key': self.brave_key,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        })

    def ask(
        self,
        prompt: str,
        system_prompt = 'You will be acting as an AI assistant named Leo created by the company Brave. Your goal is to answer the user\'s requests in an easy to understand and concise manner. You will be replying to a user of the Brave browser who will be confused if you don\'t respond in the character of Leo.\nHere are some important rules for the interaction:\n- Conciseness is important. Your responses should not exceed 6 sentences.\n- Do not say "Hey there!", go straight to the answer.\n- Always respond in a neutral and professional tone.\n- Always stay in character as an AI assistant from Brave.\n- If you are unsure how to respond, say "Sorry, I didn\'t understand that. Could you rephrase your question?"',
        model = 'llama-2-13b-chat',
        max_tokens_to_sample = 400,
        temperature = 0.2,
        top_k = -1,
        top_p = 0.999,
    ):
        json_data = {
            'max_tokens_to_sample': max_tokens_to_sample,
            'model': model,
            'prompt': f'<s>[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n{prompt} [/INST] ',
            'stop_sequences': [
                '\n\nHuman: ',
                '</response>',
            ],
            'stream': False,
            'temperature': temperature,
            'top_k': top_k,
            'top_p': top_p,
        }
        response = self.session.post(f'{self.base_url}/v1/complete', json=json_data)
        response.raise_for_status()
        return LeoCompleteResponse(**response.json())

class AsyncLeo:
    def __init__(self, brave_key = 'qztbjzBqJueQZLFkwTTJrieu8Vw3789u', base_url = 'https://ai-chat.bsg.brave.com'):
        self.brave_key = brave_key
        self.base_url = base_url
        self.session = aiohttp.ClientSession(headers={
            'x-brave-key': self.brave_key,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }, base_url=self.base_url, raise_for_status=True)

    async def ask(
        self,
        prompt: str,
        system_prompt = 'You will be acting as an AI assistant named Leo created by the company Brave. Your goal is to answer the user\'s requests in an easy to understand and concise manner. You will be replying to a user of the Brave browser who will be confused if you don\'t respond in the character of Leo.\nHere are some important rules for the interaction:\n- Conciseness is important. Your responses should not exceed 6 sentences.\n- Do not say "Hey there!", go straight to the answer.\n- Always respond in a neutral and professional tone.\n- Always stay in character as an AI assistant from Brave.\n- If you are unsure how to respond, say "Sorry, I didn\'t understand that. Could you rephrase your question?"',
        model = 'llama-2-13b-chat',
        max_tokens_to_sample = 400,
        temperature = 0.2,
        top_k = -1,
        top_p = 0.999,
    ):
        json_data = {
            'max_tokens_to_sample': max_tokens_to_sample,
            'model': model,
            'prompt': f'<s>[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n{prompt} [/INST] ',
            'stop_sequences': [
                '\n\nHuman: ',
                '</response>',
            ],
            'stream': False,
            'temperature': temperature,
            'top_k': top_k,
            'top_p': top_p,
        }
        async  with self.session.post('/v1/complete', json=json_data) as response:
            return LeoCompleteResponse(**await response.json())

    async def close(self):
        await self.session.close()

if __name__ == '__main__':
    leo = Leo()
    response = leo.ask('What is the weather like today?')
    print(response.completion)

    import asyncio
    async def main():
        leo = AsyncLeo()
        response = await leo.ask('What is the weather like today?')
        print(response.completion)
        await leo.close()
    asyncio.run(main())