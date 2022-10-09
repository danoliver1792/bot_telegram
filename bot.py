import telebot

CHAVE_API = '#####' # Chave API gerada no Telegram

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=['opcao1'])
def opcao1(message):
    textMessage = '''
    O Danrlei foi notificado e responderá em breve
    Você também pode entrar em contato por:
    email: danrlei.jesus@hotmail.com
    WhatsApp: https://wa.me/+5541989025568
    '''
    bot.send_message(message.chat.id, textMessage)


@bot.message_handler(commands=['opcao2'])
def opcao2(message):
    bot.send_message(message.chat.id, 'Valeu! Danrlei mandou um abraço de volta')


def check(message):
    return True
    

# Criando um decoretor para respostas de mensagens (definindo quando bot.polling será executado)
@bot.message_handler(func=check)
def answer(message):
    textMessage = '''
    Escolha uma opção para continuar (clique no item):
    /opcao1 Entrar em contato com Danrlei
    /opcao2 Mandar um abraço para o Danrlei
    
    Por favor, escolha uma das opções acima
    '''
    bot.reply_to(message, textMessage)
    
    
bot.polling() # Loop que faz o bot conversar o tempo inteiro no Telegram