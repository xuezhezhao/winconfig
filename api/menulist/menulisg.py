import requests
import json
import urllib3
from api.login.login import Login
urllib3.disable_warnings()
from common.readconfig import ReadFile
from common.writetoken import readToken

host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
class MenuList():
    def getUserMenuList(self,source="3"):     # 获取菜单列表
        url=host+'/api/zh-cn/common/getUserMenuList'
        data={"menuId":"0",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"source":source}
              }
        headers = {'Content-Type': 'application/json','Authorization':readToken()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result

if __name__=='__main__':
    print(MenuList().getUserMenuList().json())