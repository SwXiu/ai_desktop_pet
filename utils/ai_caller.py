import openai
import requests

def call_ai_api(messages, model="gpt-4o", temperature=0.7, api_key=None, api_url=None):
    if model.startswith("gpt"):
        return call_openai(messages, model, temperature, api_key)
    elif model.startswith("deepseek"):
        return call_deepseek(messages, model, temperature, api_key, api_url)
    elif model.startswith("local"):
        return call_local_model(messages, model, temperature, api_url)
    else:
        return "[AI错误] 不支持的模型类型"

def call_openai(messages, model, temperature, api_key=None):
    try:
        if api_key:
            openai.api_key = api_key

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[OpenAI错误] {e}"

def call_deepseek(messages, model, temperature, api_key, api_url):
    try:
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        resp = requests.post(api_url, headers=headers, json=payload, timeout=15)
        data = resp.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[DeepSeek错误] {e}"

def call_local_model(messages, model, temperature, api_url):
    try:
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }

        resp = requests.post(api_url, json=payload, timeout=10)
        data = resp.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[本地模型错误] {e}"