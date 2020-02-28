import telegram
from telegram.ext import Updater, CommandHandler

class TelegramBot:
   def __init__(self, name, token):
       self.core = telegram.Bot(token)
       self.updater = Updater(token)
       self.id = '3493023403' # 아이디는 예시입니다.
       self.name = name

   def sendMessage(self, text):
       self.core.sendMessage(chat_id = self.id, text=text)

   def stop(self):
       self.updater.start_polling()
       self.updater.dispatcher.stop()
       self.updater.job_queue.stop()
       self.updater.stop()

class ChatBot(TelegramBot):
   def __init__(self):
       self.token = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11' # 토큰도 예시입니다.
       TelegramBot.__init__(self, '에이치엘비', self.token)
       self.updater.stop()

   def add_handler(self, cmd, func):
       self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

   def start(self):
       self.sendMessage('엘비봇이 잠에서 깨어납니다.')
       self.updater.start_polling()
       self.updater.idle()
