import requests
import json
import urllib3
from api.login.login import Login
urllib3.disable_warnings()
from common.readconfig import ReadFile

host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
class DeviceStatus():
    def getDevice(self,sitekey):                #获取设备列表
        url = host + '/api/zh-cn/DataOperations/getDevice'
        data = {"menuId":"1000501",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{"siteKey":sitekey,
                          "disconnectTime":15}
                }
        headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getDeviceDetail(self,sitekey):                   #获取设备详情
        url = host + '/api/zh-cn/DataOperations/getDeviceDetail'
        data = {"menuId":"1000501",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{"siteKey":sitekey,
                          "disconnectTime":15}
                }
        headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result




if __name__=='__main__':
    pass

