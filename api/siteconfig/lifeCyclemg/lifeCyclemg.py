import requests
import json
import urllib3
from api.login.login import Login
urllib3.disable_warnings()
from common.readconfig import ReadFile

host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
class LifeCycle():
    def Time_GetBusinessList(self):     # 查看生命周期业务名称
        url=host+'/api/zh-cn/site/Time_GetBusinessList'
        data={"menuId":"1000207",
              "userId":Login().get_userid(),
              "params":{}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def Time_GetDataList(self,sitekey,business):     # 查看场所业务生命周期
        url=host+'/api/zh-cn/site/Time_GetDataList'
        data={"menuId":"1000207",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"SiteKey":sitekey,
                        "Business":business,
                        "PageSize":10,
                        "PageIndex":1}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def Time_DeleteSingleInfo(self,sitekey):     #    删除
        url=host+'/api/zh-cn/site/Time_DeleteSingleInfo'
        data={"menuId":"1000502",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "Params":{"ParamOne":"P00001S00001",
                        "ParamTwo":"",
                        "ParamThree":"2022-09-08 00:00:00",
                        "ParamFour":"",
                        "Business":"dbo.Traffic_Sites_History"}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result



    def Time_DeleteInfo(self,sitekey):     #    清空场所生命周期
        url=host+'/api/zh-cn/site/Time_DeleteInfo'
        data={"menuId":"1000207",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "Params":{"SiteKey":sitekey}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result



if __name__=='__main__':
    pass

