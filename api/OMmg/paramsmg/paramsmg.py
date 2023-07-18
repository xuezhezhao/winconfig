import requests
import json
import urllib3
from api.login.login import Login
urllib3.disable_warnings()
from common.readconfig import ReadFile

host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
class ParamsMg():
    def getMenuNameList(self,type):     # 获取系统参数列表
        url=host+'/api/zh-cn/SystemParameter/getMenuNameList'
        data={"menuId":"1000508",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"menuName":"",
                        "PageIndex":1,
                        "PageSize":"10"}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def saveEdit(self,paracode,cn_name,en_name,tw_name):     # 编辑属性
        url=host+'/api/zh-cn/SystemParameter/saveEdit'
        data={"menuId":"1000508",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"menuId":"1000504",
                        "menuName_CN":"标客点位数据",
                        "menuName_EN":"Tender Point Data",
                        "menuName_TW":"标客点位数据"}
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

