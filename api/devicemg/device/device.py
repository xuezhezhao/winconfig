import requests
import json
import urllib3
from api.login.login import Login
urllib3.disable_warnings()
from common.readconfig import ReadFile

host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
class Devicemg():
    def addDevice(self,sitekey,devicetype,num):     # 新增设备
        url=host+'/api/zh-cn/Device/addDevice'
        data={"menuId":"1000301",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"siteKey":sitekey,
                        "deviceType":devicetype,
                        "num":num,
                        "trafficCompany":"H"}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def editDevice(self,devicekey,hostname,deviceid,crearetime,modifytime,enable,detail=None,channels_enable=0,camerakey='',relationcamera=None):     # 编辑设备
        url=host+'/api/zh-cn/Device/editDevice'
        data={"menuId":"1000301",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "Params":{"deviceKey":devicekey,
                        "hostName":hostname,
                        "sn":"none",
                        "deviceId":deviceid,
                        "ip":None,
                        "port":"7000",
                        "detail":detail,
                        "deviceLocation":None,
                        "devInstallTime":None,
                        "devHwVersion":None,
                        "devSwVersion":None,
                        "devDspVersion":None,
                        "contanct":None,
                        "createTime":crearetime,
                        "modifyTime":modifytime,
                        "enable":enable,"connectName":"super",
                        "connectPassword":"passme",
                        "channels":[{"enable":channels_enable,
                                     "channel":0,
                                     "cameraKey":camerakey,
                                     "relationCamera":relationcamera
                                     }]
                        }
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result

    def deleteDevice(self,devicekey):     # 删除设备
        url=host+'/api/zh-cn/Device/deleteDevice'
        data={"menuId":"1000301",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"deviceKey":devicekey}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getDeviceList(self,sitekey):     # 获取设备列表
        url=host+'/api/zh-cn/Device/getDeviceList'
        data={"menuId":"1000301",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"SiteKey":sitekey,
                        "deviceStatus":"-1",
                        "hostName":"",
                        "PageIndex":1,
                        "PageSize":10}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getSingleDeviceList(self,devicekey):     # 查看设备信息
        url=host+'/api/zh-cn/Device/getSingleDeviceList'
        data={"menuId":"1000201",
              "userId":"398d8169-752e-4f61-9f95-d2ce2b34759e",
              "lang":"zh-cn",
              "params":{"deviceKey":devicekey}}
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getSiteDeviceKeyList(self,sitekey):     # 获取场所下设备编码列表
        url=host+'/api/zh-cn/Device/getSiteDeviceKeyList'
        data={"menuId":"1000201",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"siteKey":sitekey}}
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result

    def getDeviceTypeList(self):     # 获取设备类型列表
        url=host+'/api/zh-cn/Device/getDeviceTypeList'
        data={"menuId":"1000201","userId":Login().get_userid(),"lang":"zh-cn","params":{}}
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def editDeviceHostName(self,devicekey,name):     # 修改设备点码
        url=host+'/api/zh-cn/Device/editDeviceHostName'
        data={"menuId":"1000201",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"deviceKey":devicekey,
                        "hostName":name}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def getSiteCamera(self,sitekey):     # 查看场所摄像头
        url=host+'/api/zh-cn/Device/getSiteCamera'
        data={"menuId":"1000201",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"siteKey":sitekey}
              }
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def judgeCameraIsUsed(self,devicekey,camerakey):     #
        url=host+'/api/zh-cn/Device/getSiteCamera'
        data={"menuId":"1000201",
              "userId":Login().get_userid(),
              "lang":"zh-cn",
              "params":{"deviceKey":devicekey,
                        "cameraKey":camerakey}}
        headers = {'Content-Type': 'application/json','Authorization':Login().get_cookie()}
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result






if __name__=='__main__':
    print(Devicemg().addDevice('P00001','T0901E',2))

