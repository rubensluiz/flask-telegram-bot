from flask import Flask, request, jsonify
import json
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, World!'

@application.route('/telebot', methods=['POST'])
def telebot():
    """endpoint responsible to parse and respond bot webhook"""
    payload = json.loads(request.data)
    message = payload.get('message', payload.get('edited_message',''))
    msg_from = message.get('from')
    user_id = msg_from.get('id')
    user_first_name = msg_from.get('first_name','')
    user_last_name = msg_from.get('last_name','')
    user_is_bot = msg_from.get('is_bot')
    chat = message.get('chat')
    chat_id = chat.get('id')
    command = message.get('text')
    
    if user_is_bot or message == '':
        return jsonify({'method': 'sendMessage','chat_id' : chat_id,'text': 'Sorry I can\'t answer you!'})
    
    bot_response = {
                    'method': 'sendMessage',
                    'chat_id' : chat_id,
                    'text': f'[{user_first_name} {user_last_name}](tg://user?id={user_id}) {command}',
                    'parse_mode':'Markdown',
                }

    return jsonify(bot_response)