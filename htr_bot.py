# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:00:12 2019

@author: tanma
"""
import cv2
import logging
import pytesseract
import urllib.request

from telegram.ext import Updater, MessageHandler, Filters
 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def download_image(url,name):
    fullname = str(name)+".jpeg"
    urllib.request.urlretrieve(url,fullname)


def some_func(bot, update):
    pass
    if not update.effective_message.photo:
        update.effective_message.reply_text(text = "This bot is only capable of Computer Vision Tasks!")
        update.effective_message.reply_text(text = "Getting Self Aware Now!")
    else:
        msg = update.effective_message
        file_id = msg.photo[-1].file_id
        photo = bot.get_file(file_id)
        download_image(photo["file_path"],'wassup')
        text = pytesseract.image_to_string(cv2.imread("wassup.jpeg"), lang = "eng")
        update.effective_message.reply_text(text = text)

        
def main():
    updater = Updater('1059913469:AAHPrHeLuqVEz-UbRezjyYJQ_swoHrQ-_QM')
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.all, some_func))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()