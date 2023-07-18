import requests
import json
import urllib3
from api.login.login import Login
urllib3.disable_warnings()
from common.readconfig import ReadFile

host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
class attribute():
    def getPropertyList(self,type):     # 获取系统属性列表（设备类型/场所类型）
        url=host+'/api/zh-cn/SystemProperty/getPropertyList'
        data={"menuId":"1000507",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"Type":type}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def save(self,paracode,cn_name,en_name,tw_name):     # 编辑属性
        url=host+'/api/zh-cn/SystemProperty/save'
        data={"menuId":"1000507",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"ParaCode":paracode,
                        "ParaName_CN":cn_name,
                        "ParaName_EN":en_name,
                        "ParaName_TW":tw_name}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def enableSystemProperty(self,paracode,value):     # 禁用/启用
        url=host+'/api/zh-cn/SystemProperty/enableSystemProperty'
        data={"menuId":"1000507",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"ParaKey":paracode,
                        "Value":value}}
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result




if __name__=='__main__':
    pass

