# coding:utf-8

import werobot
from werobot import client

from config import token, appid, appsecret, host, port, session

robot = werobot.WeRoBot(token=token, enable_session=session)
client = client.Client(appid, appsecret)


@robot.handler
def error(message, session):
    return u'''您给的内容我们暂时无法识别。。。。。

点击下面的 帮助 可以查看使用方法'''


@robot.key_click('main')
def main(message, session):
    return 'main'


@robot.subscribe
@robot.key_click('help')
def help(message, session):
    return 'help'

@robot.key_click('ls')
def ls(message, session):
    count = session.get('ls', 0) + 1
    return u'''历史推送 第%d页''' % (count,)

@robot.unsubscribe
def unsubscribe(message, session):
    return 'subscribe'


@robot.click
def click(message, session):
    return str(message.key)


@robot.text
def text(message, session):
    return u'''你输入的是: %s''' % (message.content,)


if __name__ == '__main__':
    from config import menu
    try:
        client.create_menu(menu)
    except:
        pass
    robot.run(host=host, port=port)
