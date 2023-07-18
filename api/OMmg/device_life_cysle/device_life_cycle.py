import requests
import json
import urllib3
from api.login.login import Login
urllib3.disable_warnings()
from common.readconfig import ReadFile

host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
class device_life_cycle():
    def Time_GetBusinessList(self):                #获取业务类型
        url = host + '/api/zh-cn/site/Time_GetBusinessList'
        data = {"menuId":"1000502",
                "userId":Login().get_userid(),
                "params":{}}
        headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def Time_GetDataList(self,sitekey,business):                   #获取某个场所的某个表数据
        url = host + '/api/zh-cn/site/Time_GetDataList'
        data = {"menuId":"1000502",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{"SiteKey":sitekey,
                          "Business":business,
                          "PageSize":10,
                          "PageIndex":1}
                }
        headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result




if __name__=='__main__':
    pass

