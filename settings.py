import json
import os
from pathlib import Path

from aiogram import Bot
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR.joinpath('env'))
API_TOKEN = ""

DATABASE = {
    "NAME": "",
    "USER": "",
    "PASSWORD": "",
    "HOST": "",
}

# База данных/тип postgresql, mysql
DATABASE_TYPE = "postgresql"

DATABASE_STR = ""

if DATABASE_TYPE == "postgresql":
    DATABASE_STR = f"postgresql://{DATABASE['USER']}:{DATABASE['PASSWORD']}@{DATABASE['HOST']}/{DATABASE['NAME']}"

def get_words(file_name):
    data = {}
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

WORDS = get_words(r'dictionary.json')

# Канал с отзывами
# REVIEWS_CHANNEL = ''
REVIEWS_CHANNEL = ''
# диалог с разработчиком
DEVELOPER_DIALOG = ' '
# DEVELOPER_DIALOG = ''
#NOT_WORD_DIALOG = 911357472
NOT_WORD_DIALOG = 
SITE = ''

bot = Bot(token=API_TOKEN, parse_mode='HTML')
