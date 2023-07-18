import requests
import json
import urllib3
from common.readconfig import ReadFile
from common.read_yaml import get_yaml_filepath
from common.route import *
urllib3.disable_warnings()


host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
user=ReadFile().get_key('USER','username')
password=ReadFile().get_key('USER','password')

url1=login['url']
class Login():
    def login(self,user=user,password=password):
        url = host+url1
        data = {"menuId": "",
                "userId": "",
                "lang": "zh-cn",
                "params": {"UserName": user,
                           "PassWord": password,
                           "Id": "324",
                           "Code": "564"
                           }
                }
        header = {'Content-Type': 'application/json'}
        result = requests.post(url=url, data=json.dumps(data), headers=header)
        # if result['description']=='用户异常，请联系系統管理员！':
        #     return
        return result
    def getCaptcha(self):
        url = host+'/api/zh-cn/Captcha/getCaptcha'
        data = {"menuId": "",
                "userId": "",
                "lang": "zh-cn",
                "params": {"UserName": user,
                           "PassWord": password
                           }
                }
        header = {'Content-Type': 'application/json'}
        result = requests.post(url=url, data=json.dumps(data), headers=header)
        return result


    def get_cookie(self):
        res=self.login().headers['Authorization']
        return res
    def get_userid(self):
        try:
            res = self.login().json()['msg']['userID']
        except TypeError:
            res='398d8169-752e-4f61-9f95-d2ce2b34759e'

        return res
    def get_roleid(self):
        try:
            res = self.login().json()['msg']['roleID']
        except TypeError:
            res='46A2D7E0-E525-437C-9100-4B113C1D8676'

        return res


#   {'code': '1', 'description': '用户异常，请联系系統管理员！', 'msg': None}

if __name__=='__main__':
    # pass
    print(Login().login().json())
    print(Login().get_cookie())
    print(Login().get_userid())

