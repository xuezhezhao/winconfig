import requests
import json
import urllib3
from api.login.login import Login
urllib3.disable_warnings()
from common.readconfig import ReadFile

host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
class userlogin():
    def getOperaLogList(self,type):     # 获取用户访问日志
        url=host+'/api/zh-cn/Log/getOperaLogList'
        data={"menuId":"1000601",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"Operator":"",
                        "MenuName":"",
                        "pageSize":"10",
                        "pageIndex":"1"}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result



if __name__=='__main__':
    pass

