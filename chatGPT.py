import requests

def chatGPT(question):
    url = 'https://api.openai.com/v1/completions'
    auth_token = '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'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+auth_token
    }
    myobj = {
        "model": "text-davinci-001",
        "prompt": question,
        "temperature": 0.4,
        "max_tokens": 64,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    response = requests.post(url,json = myobj,headers=headers)
    resJson = response.json()
    answer = resJson['choices'][0]['text']
    return answer