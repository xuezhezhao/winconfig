import requests
import json
import urllib3
from api.login.login import Login
urllib3.disable_warnings()
from common.readconfig import ReadFile

host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
class User():
    def getUserList(self,name,roleid):     # 查询用户列表
        url=host+'/api/zh-cn/User/getUserList'
        data={"menuId":"1000401",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"RealName":"",
                        "UserId":Login().get_userid(),
                        "RoleId":roleid,
                        "PageIndex":1,
                        "PageSize":10}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getDefaultPwd(self):  # 获取新用户默认密码
        url = host + '/api/zh-cn/User/getDefaultPwd'
        data = {"menuId":"1000401",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{}
                }
        headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
    def checkUser(self,userid):  # 查看用户
        url = host + '/api/zh-cn/User/checkUser'
        data = {"menuId":"1000401",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{"UserID":userid}
                }
        headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
    def getUserRole(self):     # 获取用户角色
        url=host+'/api/zh-cn/User/getUserRole'
        data={"menuId":"1000401",
              "userId":Login().get_userid(),
              "params":{"UserId":Login().get_userid()}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def addUser(self, username,realname,roleid,sitekey,password,email='',remark=''):  # 添加用户
        url = host + '/api/zh-cn/User/addUser'
        data = {"menuId":"1000401",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{"AddType":"1",
                          "UserName":username,
                          "RealName":realname,
                          "RoleId":roleid,
                          "SiteKeys":sitekey,
                          "Email":email,
                          "PhoneNumber":"",
                          "Remark":remark,
                          "PassWord":password,
                          "Source":"3"}
                }
        headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)

        def editUser(self,userid,sitekey,username,realname,roleid, email='', remark=''):  # 编辑用户
            url = host + '/api/zh-cn/User/editUser'
            data = {"menuId":"1000401",
                    "userId":"398d8169-752e-4f61-9f95-d2ce2b34759e",
                    "lang":"zh-cn",
                    "Params":{"UserId":userid,
                              "SiteKeys":sitekey,
                              "UserName":username,
                              "RealName":realname,
                              "RoleId":roleid,
                              "Email":email,
                              "PhoneNumber":"",
                              "Remark":remark,
                              "Source":"3"}
                    }
            headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
            result = requests.post(url=url, data=json.dumps(data), headers=headers)

        def deleteUser(self, userid):  # 删除用户
            url = host + '/api/zh-cn/User/deleteUser'
            data = {"menuId":"1000401",
                    "userId":Login().get_userid(),
                    "lang":"zh-cn",
                    "params":{"UserID":userid}
                    }
            headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
            result = requests.post(url=url, data=json.dumps(data), headers=headers)
if __name__=='__main__':
    pass

