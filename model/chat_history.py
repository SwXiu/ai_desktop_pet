import json
import os

class ChatHistory:
    def __init__(self, filepath="chat_history.json"):
        self.filepath = filepath
        self.history = self.load() or []

    def load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save(self):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=4)

    def append(self, role, content):
        self.history.append({"role": role, "content": content})
        self.save()

    def clear(self):
        self.history = []
        self.save()

    def get_all(self):
        return self.history
