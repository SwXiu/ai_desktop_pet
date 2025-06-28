import json
import os

class AIProfile:
    def __init__(self, filepath="ai_profile.json"):
        self.filepath = filepath
        self.profile = self.load() or {
            "personality_prompt": "",
            "temperature": 0.7,
            "model_name": "gpt-4o",
            "emotion_state": None,
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
        self.profile.update(new_info)
        self.save()

    def get_personality_prompt(self):
        return self.profile.get("personality_prompt", "")

    def get_temperature(self):
        return self.profile.get("temperature", 0.7)

    def get_model_name(self):
        return self.profile.get("model_name", "gpt-4o")
    
    def get_emotion_state(self):
        return self.profile.get("emotion_state", None)

