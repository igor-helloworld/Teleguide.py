import requests
from config import gptkey, gptkey2
#chinesse open ia licience 100% real 0% fake clickbait no ads free


def donotwork(text):
    prompt = {
        "modelUri": f"gpt://{gptkey2}/yandexgpt",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "assistant",
                "text": text
            }
        ]
    }
    
    
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {gptkey}"
    }
    
    response = requests.post(url, headers=headers, json=prompt)
    result = response.json().get('result')
    return result['alternatives'][0]['message']['text']


# print(gpt("TODOS los tegs de html"))