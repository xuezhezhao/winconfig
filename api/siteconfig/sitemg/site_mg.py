import requests
import json
import urllib3
from api.login.login import Login
urllib3.disable_warnings()
from common.readconfig import ReadFile
from common.writetoken import readToken


host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
class SiteMg():
    def getUserSite(self):     # 获取场所数据
        url=host+'/api/zh-cn/site/getUserSite'
        data={"menuId":"1000201",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"beginSiteType":"-1",
                        "endSiteType":"300",
                        "keyWord":"",
                        "businessKey":"",
                        "siteKey":""
                        }
              }
        headers = {'Content-Type': 'application/json','Authorization':readToken()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def GetUserSiteOfLazy(self,begin,end,sitekey):     # 获取场所下数据
        url=host+'/api/zh-cn/site/GetUserSiteOfLazy'
        data={"menuId":"1000201",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"beginSiteType":begin,
                        "endSiteType":end,
                        "source":"3",
                        "keyWord":"",
                        "siteKey":sitekey}
              }
        headers = {'Content-Type': 'application/json','Authorization':readToken()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result

    def getType(self,sitetype=100):             #获取场所下可添加场所类型
        url=host+'/api/zh-cn/site/getType'
        data={"menuId":"1000201",
              "userId":'398d8169-752e-4f61-9f95-d2ce2b34759e',
              "lang":"zh-cn",
              "params":{"siteType":sitetype}
              }
        headers = {'Content-Type': 'application/json', 'Authorization': readToken()}
        result=requests.post(url=url, data=json.dumps(data), headers=headers)
        return result

    def getStatus(self,status='-1'):             #获取场所下可添加场所类型
        url=host+'/api/zh-cn/site/getStatus'
        data={"menuId":"1000201",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"siteStatus":status}
              }
        headers = {'Content-Type': 'application/json', 'Authorization': readToken()}
        result=requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getNewsitekey(self,sitekey,sitetype):     # 获取要添加场所的sitekey
        url=host+'/api/zh-cn/site/getNewSiteKey'
        data={"menuId": "1000201",
              "userId": Login().get_userid(),
              "lang": "zh-cn",
              "params": {"siteKey":sitekey,
                    "siteType":sitetype }
              }
        headers = {'Content-Type': 'application/json','Authorization':readToken()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result

    def getPositionInfo(self,type,parentid):     # 获取城市信息
        url=host+'/api/zh-cn/common/getPositionInfo'
        data={"menuId":"1000101",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"Type":type,
                        "ParentId":parentid}
              }
        headers = {'Content-Type': 'application/json','Authorization':readToken()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result



    def addsite(self,sitekey,sitetype,opendate,name,city,regid,proid,cityid,areaid,staus,area):           #  添加场所
        url = host+'/api/zh-cn/site/addSite'
        data ={"menuId":"1000101",
               "userId":Login().get_userid(),
               "lang":"zh-cn",
               "params":{"siteKey":sitekey,
                         "siteType":sitetype,
                         "parentId":1,
                         "customerId":"",
                         "openDate":opendate,
                         "siteName":name,
                         "city":city,
                         "Country_Id":100000,
                         "Region_Id":regid,
                         "Province_Id":proid,
                         "City_Id":cityid,
                         "Area_Id":areaid,
                         "siteStatus":staus,
                         "siteImage":"",
                         "area":area,
                         "address":"",
                         "staffNo":0,
                         "domainName":"|",
                         "indexNo":""}
               }
        headers = {'Content-Type': 'application/json','Authorization':readToken()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result

    def deleteSite(self,sitekey):           #  删除场所
        url = host+'/api/zh-cn/site/deleteSite'
        data = {"menuId":"1000201",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{"siteKey":sitekey
                          }
                }
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = readToken()
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getSites(self,sitekey,name="",status=-1,sitetype=-1):           #  查看场所
        url = host+'/api/zh-cn/site/getSites'
        data = {"menuId":"1000201",
                "userId": Login().get_userid(),
                "lang":"zh-cn",
                "params":{"siteKey":sitekey,
                          "siteName":name,
                          "siteStatus":status,
                          "SiteType":sitetype,
                          "pageIndex":1,
                          "pageSize":10}
                }
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = readToken()
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getSingleSite(self,sitekey):           #  查看单个场所
        url = host+'/api/zh-cn/site/getSingleSite'
        data = {"menuId":"1000201",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{"siteKey":sitekey}
                }
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = readToken()
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def editSite(self,sitekey,sitetype,opendate,name,city,regid,proid,cityid,areaid,area):           #  编辑场所
        url = host+'/api/zh-cn/site/editSite'
        data = {"menuId":"1000101",
                "userId":"398d8169-752e-4f61-9f95-d2ce2b34759e",
                "lang":"zh-cn",
                "params":{"siteKey":sitekey,
                          "siteType":sitetype,
                          "parentId":1,
                          "customerId":None,
                          "openDate":opendate,
                          "siteName":name,
                          "city":city,
                          "Country_Id":100000,
                          "Region_Id":regid,
                          "Province_Id":proid,
                          "City_Id":cityid,
                          "Area_Id":areaid,
                          "siteStatus":"1",
                          "siteImage":"",
                          "area":area,
                          "address":"",
                          "staffNo":0,
                          "domainName":"|",
                          "indexNo":None}}
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = readToken()
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result



    def getHistory(self, sitekey):  # 历史查询
        url = host + '/api/zh-cn/site/getHistory'
        data = {"menuId":"1000201",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{"siteKey":sitekey,
                          "PageIndex":1,
                          "PageSize":10}
                }
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = readToken()
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def relationCamera(self, sitekey,direction,cameraname,camerakey,isvirtual=1):  # 关联摄像头
        url = host + '/api/zh-cn/site/relationCamera'
        data = {"menuId":"1000201",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{"siteKey":sitekey,
                          "direction":direction,
                          "cameraKeys":[{"cameraName":cameraname,
                                         "cameraKey":camerakey,
                                         "isVirtual":isvirtual}]
                          }
                }
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = readToken()
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getSiteCamera(self, sitekey):  # 查看场所下未关联的摄像头
        url = host + '/api/zh-cn/site/getSiteCamera'
        data = {"menuId":"1000201",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{"siteKey":sitekey}
                }
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = readToken()
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getRelationCamera(self, sitekey,camerakey='',direction='-1'):  # 查看场所下关联的摄像头
        url = host + '/api/zh-cn/site/getRelationCamera'
        data = {"menuId":"1000201",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{"siteKey":sitekey,
                          "cameraKey":camerakey,
                          "direction":direction,
                          "PageIndex":1,
                          "PageSize":10}
                }
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = readToken()
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getRelationCameraHistory(self, sitekey,camerakey):           # 摄像头历史查询
        url = host + '/api/zh-cn/site/getRelationCameraHistory'
        data = {"menuId":"1000201",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{"siteKey":sitekey,
                          "cameraKey":camerakey,
                          "isVirtual":1,
                          "PageIndex":1,
                          "PageSize":10}
                }
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = readToken()
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def deleteRelationCamera(self, sitekey,camerakey,direction):           #解绑摄像头
        url = host + '/api/zh-cn/site/deleteRelationCamera'
        data = {"menuId":"1000201",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{"siteKey":sitekey,
                          "cameraKey":camerakey,
                          "isVirtual":direction}
                }
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = readToken()
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result




#   {'code': '1', 'description': '用户异常，请联系系統管理员！', 'msg': None}

if __name__=='__main__':
    a=SiteMg().getNewsitekey('G00001','200').json()
    print(a)
    print(SiteMg().getSites('G00001').json())
