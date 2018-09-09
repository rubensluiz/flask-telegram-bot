# Simple flask app to respond to telegram webhook
These simple app exposes a endpoint that just echoes back the issued text. It is used for test and study purpose.

## Setting up a telegram bot
There is a nice [tutorial](https://core.telegram.org/bots#6-botfather) on telegram's APIs webpage that helps you to create your own bot using botFather bot.

### Setting up a telegram bot webhook
After create your bot, you will need the bot's token to setup it's webhook.

A https endpoint is needed to your webhook work properly, if you don't have a public https web server you can use [ngrok](https://ngrok.com) for tests purposes.

To setup your webhook you can use curl command by issuing:

curl -F "url=https://<bot_webhook_url>/telebot" https://api.telegram.org/bot<bot_tokenid>/setWebhook

### Docker
You can build a docker container image by using a Dockerfile on these repo, or you can pull rubensluiz/flask-telegram-bot:latest image from dockerhub, or even using docker-compose up