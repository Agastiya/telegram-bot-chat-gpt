# Telegram Bot use ChatGPT

## About
In this project I integrated the chatGPT with a telegram bot. The goal is we can use chatGPT more simply with telegram we send messages to other people. We will use ChatGPT API FREE Reverse Proxy for learning purpose. This is just a fun project, Enjoy.

## Getting Started
We will prepare this project, starting from Creating telegram bot installation, and running the code.

### Dependencies
* Python 3.11.6

### Create a Bot
We have to create telegram bot first, the step is :
* Open Telegram App.
* Connect to BotFather. search for "@BotFather" in the Telegram app and click on the result to start a conversation.
* In the conversation with BotFather, select the "New Bot" option to start creating your new bot. BotFather will guide you through the rest of the process.
* Next, BotFather will ask you to provide a name for your bot. Choose a name that accurately reflects the purpose of your bot and is easy to remember.
* Next, BotFather will ask you to choose a username for your bot. This username will be used to create a unique URL that people can use to access your bot. Choose a username that is easy to remember and related to your bot's purpose.
* Lasty, Create and save Token from your Bot. The token will be use in the program.

### Getting API KEY
* For get the API key, you need to join discord and generate the key. (follow the steps of [ChatGPT API FREE Reverse Proxy](https://github.com/PawanOsman/ChatGPT?tab=readme-ov-file#how-to-use-chatgpt-api-reverse-proxy) )
* Make sure you store the keys well.

### Installation
Several stages that need to be prepared at this stage are as follows :

* Clone this repository

        git clone https://github.com/Agastiya/telegram-bot-chat-gpt.git

* Create .env file
        
    - You can clone **.env.example** and rename the file into **.env**. 
    - After that you have to set **API_KEY** and **TOKEN_TELEGRAM_BOT** from the steps we have obtained previously
    - Save the file.

* Install the required libraries

        pip install -r requirement.txt

### Executing Program
Once all the steps are complete, **it's showtime**

    python app.py

ensure the program running well. Now you can test from your bot. Send **/start** for the first time, then you can ask question.

## Acknowledgments
* [ChatGPT API FREE Reverse Proxy](https://github.com/PawanOsman/ChatGPT?tab=readme-ov-file#how-to-use-chatgpt-api-reverse-proxy)