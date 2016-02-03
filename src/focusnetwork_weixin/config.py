# coding:utf-8

# 必须
token = 'token'
host = '0.0.0.0'
port = 8888
session = True

# 非必须
appid = 'appid'
appsecret = 'appsecret'

menu = {
    "button": [
        {
            "type": "click",
            "name": u"首页",
            "key": "main"
        }, {
            "name": u"一起学编程",
            "sub_button": [
                {
                    "type": "click",
                    "name": u"Shell",
                    "key": "bc_shell"
                }, {
                    "type": "click",
                    "name": u"Python",
                    "key": "bc_python"
                }, {
                    "type": "click",
                    "name": u"C",
                    "key": "bc_c"
                }, {
                    "type": "click",
                    "name": u"其他",
                    "key": "bc_qita"
                }
            ]
        }, {
            "name": u"服务",
            "sub_button": [
                {
                    "type": "click",
                    "name": u"nginx",
                    "key": "fw_nginx"
                }, {
                    "type": "click",
                    "name": u"apache",
                    "key": "fw_apache"
                }, {
                    "type": "click",
                    "name": u"mysql",
                    "key": "fw_mysql"
                }, {
                    "type": "click",
                    "name": u"其他",
                    "key": "fw_qita"
                }
            ]
        }, {
            "type": "click",
            "name": u"帮助`",
            "key": "help"
        }
    ]
}
