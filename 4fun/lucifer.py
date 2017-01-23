# imports
import os
import telepot
import time
# end

def handle(msg):
    # variaveis 1
    id = msg['from']['id']
    chat_id = msg['chat']['id']
    commands = ['/help', '/id', '', '']
    command = msg['text']
    user_user = '@' + msg['from']['username']
    username = msg['from']['first_name']
    username1 = "@" + username
    # end

    # comandos
    if command in commands:
        if command == '/help':
            bot.sendMessage(chat_id, 'Lucifer BOT - beta - #PirateSec\n\nCoded by: \n[*] @digitalgangsta\n[*] @b4nned\n[*] @BBtamraS\n[*] @tsohleirbag \n\nFunctions:\n/id - Exibe sua ID\n/star+ - Envia uma star para o usuario\n/star- - Envia uma star negativa para o usuario\n/help - Exibe o menu de ajuda')
        elif command == '/id':
            bot.sendMessage(chat_id, '%s |ID > %s' % (user_user, id))
    # end

    # printa o comando enviado no terminal
    print 'Comando enviado> %s' % command
    # end

    # variaveis 2
    sender = msg['from']['id']
    reply_id = msg['reply_to_message']['from']['id']
    reply = '@' + msg['reply_to_message']['from']['username']
    # end

    # comandos reply
    if sender:
        if command == '/star+':
            if (sender != reply_id):
                bot.sendMessage(chat_id, 'Usuario %s recebeu 1 star! :) | id: %s' % (reply, reply_id))
            elif (sender == reply_id):
                bot.sendMessage(chat_id, 'Impossivel dar stars para si mesmo | id: %s' % reply_id)
        elif command == '/star-':
            if (sender != reply_id):
                bot.sendMessage(chat_id, 'Usuario %s recebeu 1 star negativa! :( | id: %s' % (reply, reply_id))
            elif (sender == reply_id):
                bot.sendMessage(chat_id, 'Impossivel dar stars para si mesmo | id: %s' % reply_id)
    # end

# API + Start
bot = telepot.Bot('API')
bot.message_loop(handle)
print 'Online!'
# end

# mantem o bot rodando
while 1:
    pass
# end
