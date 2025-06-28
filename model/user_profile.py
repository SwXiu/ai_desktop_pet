import json
import os

class UserProfile:
    def __init__(self, filepath="user_profile.json"):
        self.filepath = filepath
        self.profile = self.load() or {
            "nickname": None,
            "likes": [],
            "dislikes": [],
            "special_requests": []
        }

    def load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        return None

    def save(self):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.profile, f, ensure_ascii=False, indent=4)

    def update(self, new_info: dict):
        for k, v in new_info.items():
            if isinstance(v, list):
                self.profile[k] = list(set(self.profile.get(k, []) + v))
            else:
                self.profile[k] = v
        self.save()

    def get_prompt(self):
        prompt = "以下是用户的重要信息：\n"
        for k, v in self.profile.items():
            prompt += f"{k}: {v}\n"
        return prompt

    def clear(self):
        self.profile = {
            "nickname": None,
            "likes": [],
            "dislikes": [],
            "special_requests": []
        }
        self.save()
