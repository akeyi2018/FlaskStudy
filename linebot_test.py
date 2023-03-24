from linebot import LineBotApi
from linebot.models import TextSendMessage

def main():
    token = "4DCMd5YjF21WwGEve2vM0733BamgnlnE5WsDvOUXMLjo++ofQLC+bNktDToGc8m2C908V3p5QAL1aBkgF1bdRivTww06EVeQpFdk3lQvPkLIzZEHLbZBnWVCUkaS1Rvv+1o6UCJzVSM2XVOUrRGOQwdB04t89/1O/w1cDnyilFU="
    user_id = 'U79b8610c5f077f92f42752872b967983'
    lb = LineBotApi(token)
    message = TextSendMessage(text='おはよう💛')
    lb.push_message(user_id, messages=message)

if __name__ == '__main__':
    main()

