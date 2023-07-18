import requests
import json
import urllib3
from api.login.login import Login
urllib3.disable_warnings()
from common.readconfig import ReadFile

host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
class Camera():
    def getCounter(self):  # 获取计数器
        url = host + '/api/zh-cn/camera/getCounter'
        data = {"menuId":"1000202","userId":Login().get_userid(),"lang":"zh-cn"}
        headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getCounterType(self):  # 获取计数器类型
        url = host + '/api/zh-cn/camera/getCounterType'
        data = {"menuId":"1000202","userId":Login().get_userid(),"lang":"zh-cn"}
        headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getDataType(self):  # 获取计数器规格
        url = host + '/api/zh-cn/camera/getDataType'
        data = {"menuId":"1000202","userId":Login().get_userid(),"lang":"zh-cn"}
        headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getVirCameraApplyScope(self):  # 获取适用范围
        url = host + '/api/zh-cn/camera/getVirCameraApplyScope'
        data = {"menuId":"1000202","userId":Login().get_userid(),"lang":"zh-cn"}
        headers = {'Content-Type': 'application/json', 'Authorization': Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def addCamera(self,sitekey,num):     # 新增摄像头
        url=host+'/api/zh-cn/camera/addCamera'
        data={"menuId":"1000303",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"siteKey":sitekey,
                        "num":num,
                        "isremove":"0",
                        "CompanyCode":"1",
                        "CompanyName":"汇纳"}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def searchCamera(self,sitekey):     # 查询摄像头
        url=host+'/api/zh-cn/camera/searchCameraList'
        data={"menuId":"1000303",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"siteKey":sitekey,
                        "deviceKey":"",
                        "cameraKey":"",
                        "cameraName":"",
                        "status":"-1",
                        "ip":"",
                        "pageIndex":"1",
                        "pageSize":"10"}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def deleteCamera(self,camerakey):     # 删除摄像头
        url=host+'/api/zh-cn/camera/deleteCamera'
        data={"menuId":"1000303",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"cameraKey":camerakey}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def editCamera(self,camerakey,cameraname,cameraalias,sitekey):     # 编辑摄像头别名
        url=host+'/api/zh-cn/camera/editCamera'
        data={"menuId":"1000303",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"cameraKey":camerakey,
                        "channelId":None,
                        "cameraName":cameraname,
                        "cameraAlias":cameraalias,
                        "SiteKey":sitekey}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getVirCameraLs(self,camerakey):     # 获取摄像头下的虚拟探头
        url=host+'/api/zh-cn/camera/getVirCameraLs'
        data={"menuId":"1000202",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"cameraKey":camerakey}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def addVirCameraLs(self,camerakey,counternum,datatype,virnumber,businesstype):     # 添加虚拟探头
        url=host+'/api/zh-cn/camera/addVirCameraLs'
        data={"menuId":"1000202",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"cameraKey":camerakey,
                        "virCameras":[{"counterNum":counternum,
                                       "dataType":datatype,
                                       "virnumber":virnumber,
                                       "coordinateX":"0",
                                       "coordinateY":"0",
                                       "businessType":businesstype
                                       }]
                        }
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def cameraEnable(self,camerakey,enable):     # 使能/禁止摄像头
        url=host+'/api/zh-cn/camera/cameraEnable'
        data={"menuId":"1000303",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"cameraKey":camerakey,
                        "enable":enable}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result




if __name__=='__main__':
    pass

