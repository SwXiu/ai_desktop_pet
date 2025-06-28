from controller.ai_client_base import AIClientBase
from utils.ai_caller import call_ai_api

class DeepSeekChat(AIClientBase):
    def __init__(self, api_url: str, api_key: str, temperature: float = 0.7, personality_prompt: str = "", model_name="deepseek-1"):
        self.api_url = api_url
        self.api_key = api_key
        self.temperature = temperature
        self.personality_prompt = personality_prompt
        self.model_name = model_name
        self.history = []

    def set_temperature(self, temp: float):
        self.temperature = temp

    def set_personality_prompt(self, prompt: str):
        self.personality_prompt = prompt

    def reset_history(self):
        self.history = []

    def chat(self, message: str) -> str:
        messages = [{"role": "system", "content": self.personality_prompt}]
        messages.extend(self.history)
        messages.append({"role": "user", "content": message})

        reply = call_ai_api(
            messages=messages,
            model=self.model_name,
            temperature=self.temperature,
            api_key=self.api_key,
            api_url=self.api_url,
        )

        self.history.append({"role": "user", "content": message})
        self.history.append({"role": "assistant", "content": reply})
        return reply
