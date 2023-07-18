import requests
import json
# import urllib3
from api.login.login import Login
# urllib3.disable_warnings()
from common.readconfig import ReadFile

host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Indpbm5lciIsIm5hbWUiOiJCdWlsZGluZyBhIGRhdGEgcGxhdGZvcm0gdGhhdCBjb25uZWN0cyBicmljay1hbmQtbW9ydGFyIGJ1c2luZXNzZXMiLCJhY3QiOiJhZG1pbiIsIm5iZiI6MTY3NTMxNDUwNSwiZXhwIjoxNjc1MzIxNzA1LCJpc3MiOiJ3aW5uZXIiLCJhdWQiOiJ3aW5jb25maWcifQ.W4CIzXOUrl7rrXrrFfDX-UjKh5-Xl0jSHQrAIDVopNc'
class MapConfig():
    def getBusinessData(self):  # 获取业务类型
        url = host + '/api/zh-cn/MapConfig/getBusinessData'
        data = {"menuId":"1000701","userId":Login().get_userid(),"lang":"zh-cn","params":{}}
        # headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        headers = {'Content-Type': 'application/json', 'Authorization':token }
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getSiteNavigations(self):  # 获取场所类型
        url = host + '/api/zh-cn/site/getSiteNavigations'
        data = {"menuId":"0","userId":Login().get_userid(),"lang":"zh-cn",
                "params":{"siteTypeLimit":"700",
                          "siteTypeLimitTop":"100"}
                }
        # headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result




if __name__=='__main__':
    # pass
    print(MapConfig().getBusinessData().json())

