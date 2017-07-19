# coding=utf-8

import telebot

bot = telebot.TeleBot("<TOKEN>")
forwarder_list = [235274404, 136971973, 290855719, 242382379, 311300407, 363246572, 184292188]


@bot.message_handler(func=lambda message: "#matpin" in message.text)
def forward_to_matpin(message):
    if "group" in message.chat.type and str(message.chat.id) == "-1001076357496":
        send_group_forward(message)
    else:
        if "/ping" not in message.text:
            send_private_forward(message)


@bot.message_handler(commands=['ping'])
def send_ping(message):
    bot.send_message(message.chat.id, "群组 id 为 " + str(message.chat.id) + " ，用户 id 为 " + str(message.from_user.id) + " ，完毕。")


def send_group_forward(message):
    if message.from_user.id in forwarder_list:
        if message.reply_to_message is not None:
            bot.forward_message("@matpin", message.chat.id, message.reply_to_message.message_id)
            bot.send_message(message.chat.id, "已经转发过去了哟～")
        else:
            bot.reply_to(message, "咱只能转发回复的消息哟～")
    else:
        bot.reply_to(message, "你的 PY 度还不够高呢，不能转发消息哟～")


def send_private_forward(message):
    if message.from_user.id in forwarder_list:
        if message.forward_date is not None:
            bot.forward_message("@matpin", message.forward_from_chat.id, message.reply_to_message.message_id)
            bot.send_message(message.chat.id, "已经转发过去了哟～")
        else:
            bot.send_message(message.chat.id, "咱只能转发转发给咱的消息哟～")
    else:
        bot.send_message(message.chat.id, "你的 PY 度还不够高呢，不能转发消息哟～")


bot.polling()
