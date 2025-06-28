from controller.gpt_chat import GPTChat
from controller.deepseek_chat import DeepSeekChat
from controller.local_ai_chat import LocalAIChat
from model.chat_history import ChatHistory
from model.user_profile import UserProfile
from model.ai_profile import AIProfile
from controller.ai_client_base import AIClientBase

class AppManager:
    def __init__(self, config):
        self.chat_history = ChatHistory()
        self.user_profile = UserProfile()
        self.ai_profile = AIProfile()
        self.config = config

        self.ai_clients = {
            # "GPT": GPTChat(api_key=config.gpt_api_key),
            "DeepSeek": DeepSeekChat(api_url=config.deepseek_api_url, api_key=config.deepseek_api_key),
            # "LocalAI": LocalAIChat(model=config.local_model_name),
        }

        self.current_ai_name = config.default_ai_name or "GPT"
        self.current_ai = self.ai_clients[self.current_ai_name]

        self.current_ai.set_temperature(config.temperature)
        self.current_ai.set_personality_prompt(config.personality_prompt)

    def switch_ai_client(self, ai_name: str):
        if ai_name in self.ai_clients:
            self.current_ai_name = ai_name
            self.current_ai = self.ai_clients[ai_name]
            self.current_ai.set_temperature(self.config.temperature)
            self.current_ai.set_personality_prompt(self.config.personality_prompt)
            self.config.default_ai_name = ai_name
            self.config.save()
            print(f"[AI] 已切换到：{ai_name}")
        else:
            print(f"[AI] 未知模型：{ai_name}")

    def chat(self, message):
        messages = [
            {"role": "system", "content": self.ai_profile.get_personality_prompt()},
            {"role": "system", "content": self.user_profile.get_prompt()}
        ]
        messages.extend(self.chat_history.get_all())
        messages.append({"role": "user", "content": message})

        reply = call_ai_api(
            messages,
            model=self.ai_profile.get_model_name(),
            temperature=self.ai_profile.get_temperature()
        )

        self.chat_history.append("user", message)
        self.chat_history.append("assistant", reply)

        return reply

    def set_temperature(self, temp: float):
        self.config.temperature = temp
        self.current_ai.set_temperature(temp)
        self.config.save()

    def set_personality_prompt(self, prompt: str):
        self.config.personality_prompt = prompt
        self.current_ai.set_personality_prompt(prompt)
        self.config.save()

    def reset_history(self):
        pass