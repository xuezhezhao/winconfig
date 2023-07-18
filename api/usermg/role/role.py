import requests
import json
import urllib3
from api.login.login import Login
urllib3.disable_warnings()
from common.readconfig import ReadFile

host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
class Role():
    def getRoleList(self,roleid):     # 获取角色列表
        url=host+'/api/zh-cn/Role/getRoleList'
        data={"menuId":"1000401",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"RoleId":Login().get_roleid(),
                        "UserId":roleid,
                        "PageIndex":1,
                        "PageSize":10}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result

    def getRoleMenuList(self):     # 获取该角色菜单权限列表
        url=host+'/api/zh-cn/Role/getRoleMenuList'
        data={"menuId":"1000402",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"Source":"Add",
                        "UserId":Login().get_userid(),
                        "RoleId":Login().get_roleid()}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getUserSiteOfLazy(self):     # 获取该角色场所权限列表
        url=host+'/api/zh-cn/Role/getUserSiteOfLazy'
        data={"menuId":"1000402",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"Source":"3",
                        "RoleId":Login().get_roleid(),
                        "Sitekey":"G00001",
                        "SerSiteType":"",
                        "Word":"",
                        "minSiteType":"-1"}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def addRoles(self,rolename,menuid,sitekey,remark=''):     # 获取该角色场所权限列表
        url=host+'/api/zh-cn/Role/addRoles'
        data={"menuId":"1000402",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"RoleName":rolename,
                        "MenuIds":menuid,
                        "SiteKeys":sitekey,
                        "UserId":Login().get_userid(),
                        "Remark":remark}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result





if __name__=='__main__':
    pass

