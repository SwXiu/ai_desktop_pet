from model.chat_history import ChatHistory
from model.user_profile import UserProfile
from model.ai_profile import AIProfile
import json
import openai

class MemoryManager:
    def __init__(self):
        self.chat_history = ChatHistory()
        self.user_profile = UserProfile()
        self.ai_profile = AIProfile()

    def build_messages(self, user_message: str):
        messages = []

        if self.ai_profile.get_personality_prompt():
            messages.append({"role": "system", "content": self.ai_profile.get_personality_prompt()})

        profile_prompt = self.user_profile.get_prompt()
        if profile_prompt:
            messages.append({"role": "system", "content": profile_prompt})

        messages.extend(self.chat_history.get_all())

        messages.append({"role": "user", "content": user_message})

        return messages

    def append_history(self, role: str, content: str):
        self.chat_history.append(role, content)

    def update_user_memory_from_dialogue(self, dialogue_snippet: str):
        prompt = f"""
请从下面这段对话中提取用户的关键信息，返回一个 JSON：
- nickname: 用户昵称
- likes: 用户喜欢的事物（列表）
- dislikes: 用户不喜欢的事物（列表）
- special_requests: 用户特别要求（列表）

对话内容：
{dialogue_snippet}
"""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                temperature=0
            )
            new_info = json.loads(response.choices[0].message.content)
            self.user_profile.update(new_info)
        except Exception as e:
            print(f"[MemoryManager] 关键记忆抽取失败：{e}")
