import requests
import json
import urllib3
from api.login.login import Login
urllib3.disable_warnings()
from common.readconfig import ReadFile

host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Indpbm5lciIsIm5hbWUiOiJCdWlsZGluZyBhIGRhdGEgcGxhdGZvcm0gdGhhdCBjb25uZWN0cyBicmljay1hbmQtbW9ydGFyIGJ1c2luZXNzZXMiLCJhY3QiOiJ3aW5hZG1pbiIsIm5iZiI6MTY3MDM5MzU2MCwiZXhwIjoxNjcwNDAwNzYwLCJpc3MiOiJ3aW5uZXIiLCJhdWQiOiJ3aW5jb25maWcifQ.zhnbXFpkohBLsOowDc9wVDb4kyVqnSUWOAhte00H9Hc'
class attentionManage():
    def getAttentionList(self):  # 获取客流量阈值数据
        url = host + '/api/zh-cn/attentionManage/getAttentionList'
        data = {"menuId":"1000702",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{"SiteKey":"G00001",
                          "Enable":"-1"}}
        # headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        headers = {'Content-Type': 'application/json', 'Authorization':token }
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getPassFlowList(self):  # 获取关注度阈值数据
        url = host + '/api/zh-cn/attentionManage/getPassFlowList'
        data ={"menuId":"1000702",
               "userId":Login().get_userid(),
               "lang":"zh-cn",
               "params":{"SiteKey":"G00001","Enable":"-1"}}
        # headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def Save(self):  # 添加关注度
        url = host + '/api/zh-cn/attentionManage/Save'
        data ={"menuId":"1000702",
               "userId":Login().get_userid(),
               "lang":"zh-cn",
               "params":{"id":"0",
                         "SiteKey":"G00001",
                         "ThresholdKey":"",
                         "ThresholdName":"客流量阀值",
                         "Min":"1",
                         "Max":"2",
                         "Enable":1,
                         "Description":"",
                         "Type":1}}
        # headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result




if __name__=='__main__':
    pass


