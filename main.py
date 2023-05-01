
from flask import Flask
from flask import request
from flask import Response
import requests

TOKEN = "6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk"
BOT_USERNAME = "@MedicalQuizzersTeam_bot"
app = Flask(__name__)


def parse_message(message):
    print("message-->", message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id, txt


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.post(url, json=payload)
    return r


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()

        chat_id, txt = parse_message(msg)
        if txt == "hi":
            tel_send_message(chat_id, "Hello!!")

        elif txt == "/start":
              start(chat_id, start)
        elif txt == "Anatomy":
              Anatomy(chat_id)
        elif txt == "Thorax":
              Thorax(chat_id)
        elif txt == "Lower_Limb":
              Lower_Limb(chat_id)
        elif txt == "Chemistry":
              Chemistry(chat_id)
        elif txt == "Lipids":
              Lipids(chat_id)
        elif txt == "Amino_Acids":
              Amino_Acids(chat_id)
        elif txt == "Biology":
              Biology(chat_id)
        elif txt == "Genetics":
              Genetics(chat_id)
        elif txt == "Biosafety":
              Biosafety(chat_id)
        elif txt == "Histology":
              Histology(chat_id)
        elif txt == "Physics":
              Physics(chat_id)
        elif txt == "Foundations_in_Medicine":
              Foundations_in_Medicine(chat_id)
        elif txt == "English":
              English(chat_id)
        elif txt == "Computer":
              Computer(chat_id)
        elif txt == "Word":
              Word(chat_id)
        elif txt == "Excel":
              Excel(chat_id)
        elif txt == "PowerPoint":
              PowerPoint(chat_id)

        else:
            return "Welcome"
if __name__ == '__main__':
    app.run(debug=True)



def start(chat_id):

    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "Anatomy",
                    "callback_data": "ic_Anatomy"
                },
                {
                    "text": "Chemistry",
                    "callback_data": "ic_Chemistry"
                },
                {
                    "text": "Biology",
                    "callback_data": "ic_Biology"
                },
                {
                    "text": "Physics",
                    "callback_data": "ic_Physics"
                },                {
                    "text": "Foundations_in_Medicine",
                    "callback_data": "ic_Foundations_in_Medicine"
                },
                {
                    "text": "English",
                    "callback_data": "ic_English"
                },

                {
                    "text": "Computer",
                    "callback_data": "ic_Computer"
                }]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r


def Anatomy(chat_id):

    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "Thorax",
                    "callback_data": "ic_Thorax"
                },
                {
                    "text": "Lower_Limb",
                    "callback_data": "ic_Lower_Limb"

                }]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r




def Thorax(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "Lec. 5", "url": "t.me/QuizBot?start=fpswp3Wt"},
                    {"text": "Lec. 6", "url": "t.me/QuizBot?start=3O0g9Gqs"},
                    {"text": "Lec. 7", "url": "t.me/QuizBot?start=ASHUdONn"},
                    {"text": "Lec. 8", "url": "t.me/QuizBot?start=bpDrp8py"},
                    {"text": "Lec. 9", "url": "t.me/QuizBot?start=KcBdluoh"},
                ]
            ]
        }
    }

    r = requests.post(url, json=payload)

    return r



def Lower_Limb(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "Lec. 1", "url": "t.me/QuizBot?start=KSnAerW1"},
                    {"text": "Lec. 2", "url": "t.me/QuizBot?start=7LBeZXcK"},
                    {"text": "Lec. 3", "url": "t.me/QuizBot?start=rUcd3oAF"},
                    {"text": "Lec. 4", "url": "t.me/QuizBot?start=hADBFPK4"},
                ]
            ]
        }
    }

    r = requests.post(url, json=payload)

    return r

def Chemistry(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "Lipids",
                    "callback_data": "ic_Lipids"
                },
                {
                    "text": "Amino_Acids",
                    "callback_data": "ic_Amino_Acids"

                }]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r





def Lipids(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "Lec. 1", "url": "t.me/QuizBot?start=wIW97KXo"},
                    {"text": "Lec. 2", "url": "t.me/QuizBot?start=63rY64OE"},
                    {"text": "Lec. 3", "url": "t.me/QuizBot?start=e4Y32vxO"},
                    {"text": "Lec. 4", "url": "t.me/QuizBot?start=qVpFu3lT"},
                ]
            ]
        }
    }

    r = requests.post(url, json=payload)

    return r


def Amino_Acids(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "Lec. 1", "url": "t.me/QuizBot?start=qtRvWChF"},
                    {"text": "Lec. 2", "url": "t.me/QuizBot?start=VbnaHSvg"},
                    {"text": "Lec. 3", "url": "t.me/QuizBot?start=0K2d4f6N"},
                    {"text": "Lec. 4", "url": "t.me/QuizBot?start=K6U4XyT8"},
                    {"text": "Lec. 5", "url": "t.me/QuizBot?start=NlT0XlI3"},
                    {"text": "Lec. 6", "url": "t.me/QuizBot?start=kIJlKlDE"},
                    {"text": "Lec. 7", "url": "t.me/QuizBot?start=rsgBLVdN"},
                    {"text": "Lec. 8", "url": "t.me/QuizBot?start=5uHl8qWQ"},
                ]
            ]
        }
    }

    r = requests.post(url, json=payload)

    return r

def Biology(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "Genetics",
                    "callback_data": "ic_Genetics"
                },
                {
                    "text": "Biosafety",
                    "callback_data": "ic_Biosafety"
                },
                {
                    "text": "Histology",
                    "callback_data": "ic_Histology"

                }]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r

def Genetics(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "Lec. 1", "url": "t.me/QuizBot?start=QLyaqISp"},
                    {"text": "Lec. 2", "url": "t.me/QuizBot?start=rYUleSYh"},
                    {"text": "Lec. 3", "url": "t.me/QuizBot?start=NrwBrdQK"},
                ]
            ]
        }
    }

    r = requests.post(url, json=payload)

    return r





def Biosafety(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "Lec. 3", "url": "t.me/QuizBot?start=QugRDDmu"},
                    {"text": "Lec. 4", "url": "t.me/QuizBot?start=0Z5ZaNLg"},
                ]
            ]
        }
    }

    r = requests.post(url, json=payload)

    return r

def Histology(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "Lec. 1", "url": "t.me/QuizBot?start=LG5SIe1Q"},
                    {"text": "Lec. 2", "url": "t.me/QuizBot?start=2ZMkEfGL"},
                    {"text": "Lec. 3", "url": "t.me/QuizBot?start=q53fhku8"},
                    {"text": "Lec. 4", "url": "t.me/QuizBot?start=Xi9c3eNc"},
                    {"text": "Lec. 5", "url": "t.me/QuizBot?start=RBWHXq7C"},
                    {"text": "Lec. 6", "url": "t.me/QuizBot?start=wxl8ZRwP"},
                ]
            ]
        }
    }

    r = requests.post(url, json=payload)

    return r



def Physics(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "Electricity in the Body pt. 1", "url": "t.me/QuizBot?start=heXW3nFO"},
                    {"text": "Electricity in the Body pt. 2", "url": "t.me/QuizBot?start=fUl6NNwn"},
                    {"text": "Cardiovascular System pt. 1", "url": "t.me/QuizBot?start=BtkA5TjR"},

                ]
            ]
        }
    }

    r = requests.post(url, json=payload)

    return r


def Foundations_in_Medicine(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "Lec. 1", "url": "t.me/QuizBot?start=73rOWtXF"},
                    {"text": "Lec. 2", "url": "t.me/QuizBot?start=bwRmCp8t"},

                ]
            ]
        }
    }

    r = requests.post(url, json=payload)

    return r

def English(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "Lec. 10", "url": "t.me/QuizBot?start=YQ0x71uf"},
                    {"text": "Lec. 11", "url": "t.me/QuizBot?start=FbXLGBE6"},
                    {"text": "Lec. 12", "url": "t.me/QuizBot?start=BahtBJOQ"},
                    {"text": "Lec. 13", "url": "t.me/QuizBot?start=puDyoPWH"},
                    {"text": "Lec. 14", "url": "t.me/QuizBot?start=3psK3EJK"},
                ]
            ]
        }
    }

    r = requests.post(url, json=payload)

    return r


def Computer(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "Word",
                    "callback_data": "ic_Word"
                },
                {
                    "text": "Excel",
                    "callback_data": "ic_Excel"
                },
                {
                    "text": "PowerPoint",
                    "callback_data": "ic_PowerPoint"

                }]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r



def Word(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "Lec. 4", "url": "t.me/QuizBot?start=JuFo0ybS"},

                ]
            ]
        }
    }

    r = requests.post(url, json=payload)

    return r



def Excel(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "Lec. 1", "url": "t.me/QuizBot?start=lw6Es9s0"},

                ]
            ]
        }
    }

    r = requests.post(url, json=payload)

    return r



def PowerPoint(chat_id):
    url = f'https://api.telegram.org/bot6230336662:AAGVQe8AqD9bvcByjkgBq6ZqVQ69TsviETk/sendMessage'

    payload = {
        'chat_id': chat_id,
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "Lec. 1", "url": "t.me/QuizBot?start=nFPX1SaV"},
                    {"text": "Lec. 2", "url": "t.me/QuizBot?start=C16rd50S"},
                    {"text": "Lec. 3", "url": "t.me/QuizBot?start=1E9u8G0L"},
                ]
            ]
        }
    }

    r = requests.post(url, json=payload)

    return r
