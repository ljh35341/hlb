import sys
import TelegramChatBot
import scraping

def TaskB(bot, update):
    new_info = scraping.TaskA()
    for i in new_info:
        ChatBot.sendMessage(i)

ChatBot = TelegramChatBot.ChatBot()
ChatBot.add_handler('9', TaskB)  # 특수문자 ','를 사용할 경우 Error가 뜹니다. Command is not a valid bot command
ChatBot.start()