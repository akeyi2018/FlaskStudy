from linebot import LineBotApi
from linebot.models import TextSendMessage

def main():
    token = "dummy_token"
    user_id = 'dummy_user_name'
    lb = LineBotApi(token)
    message = TextSendMessage(text='おはよう💛')
    lb.push_message(user_id, messages=message)

if __name__ == '__main__':
    main()

