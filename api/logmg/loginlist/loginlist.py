import requests
import json
import urllib3
from api.login.login import Login
urllib3.disable_warnings()
from common.readconfig import ReadFile

host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
class LoginList():
    def getUserAccess(self,type):     # 获取用户访问统计
        url=host+'/api/zh-cn/Log/getUserAccess'
        data={"menuId":"1000602",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"beginDate":"2022-09-06",
                        "endDate":"2022-09-13"}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result

if __name__=='__main__':
    pass

