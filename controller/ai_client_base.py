from abc import ABC, abstractmethod

class AIClientBase(ABC):
    @abstractmethod
    def chat(self, message: str) -> str:
        pass

    @abstractmethod
    def set_temperature(self, temp: float):
        pass

    @abstractmethod
    def set_personality_prompt(self, prompt: str):
        pass

    @abstractmethod
    def reset_history(self):
        pass

    def load_state(self):
        pass

    def save_state(self):
        pass
