import unittest
# from public.base_request import BaseRequest
# from commn.read import read_excel
from api.siteconfig.sitemg.site_mg import SiteMg
from api.devicemg.camera.camera import Camera
from api.devicemg.device.device import Devicemg
from data.devicemg.VirCamera.add import addsite_key, num, counternum, datatype, businesstype
from data.devicemg.device.add import addsite_key, devicetype, num,describe

file_path = r'C:\Users\admin\Desktop\winconfig接口自动化测试数据.xlsx'


# file_path=r'C:\Users\admin\Desktop\test.xlsx'


class relation(unittest.TestCase):
    def setUp(self):
        SiteMg().addsite(addsite_key, '300', '汇纳一号店铺', 10000, '440300')
        Devicemg().addDevice(addsite_key, devicetype, num)
        Camera().addCamera(addsite_key, num)
        global camearkey
        camearkey = Camera().searchCamera(addsite_key).json()['msg']['data'][0]['cameraKey']
        cameraname = Camera().searchCamera(addsite_key).json()['msg']['data'][0]['cameraName']
        a = camearkey[1:6]
        b = 0
        for c in a:
            if c != '0':
                break
            else:
                b = b + 1
        x = a[b:len(a)]
        d = cameraname[1:6]
        e = 0
        for f in d:
            if f != '0':
                break
            else:
                e = e + 1
        y = d[e:len(d)]
        virnumber = camearkey[0] + a[b:len(a)] + cameraname[0] + d[e:len(d)] + '_' + str(counternum) + datatype
        Camera().addVirCameraLs(camearkey, str(counternum), datatype, virnumber, businesstype)

    def tearDown(self):
        Camera().deleteCamera(camearkey)
        devicekey = Devicemg().getDeviceList(addsite_key).json()['msg']['data'][0]['deviceKey']
        res = Devicemg().getSingleDeviceList(devicekey).json()['msg']
        Devicemg().editDevice(devicekey, res['hostName'], res['deviceId'], res['createTime'], res['modifyTime'], 0,
                              res['detail'])  # 修改设备使能
        result = Devicemg().deleteDevice(devicekey)
        SiteMg().deleteSite(addsite_key)

    def test_editDevice(self):
        ''' 设备管理-设备绑定摄像头'''
        devicekey = Devicemg().getDeviceList(addsite_key).json()['msg']['data'][0]['deviceKey']
        res = Devicemg().getSingleDeviceList(devicekey).json()['msg']
        result=Devicemg().editDevice(devicekey, res['hostName'], res['deviceId'], res['createTime'], res['modifyTime'], 0,
                              detail=describe,camerakey=camearkey,relationcamera=camearkey).json()['msg']['name']
        self.assertEqual(result, 'Common_Success')






if __name__ == '__main__':
    unittest.main()

