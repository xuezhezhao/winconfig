import unittest
# from public.base_request import BaseRequest
# from commn.read import read_excel
from api.siteconfig.sitemg.site_mg import SiteMg
from api.devicemg.camera.camera import Camera
from api.devicemg.device.device import Devicemg
from data.devicemg.VirCamera.add import addsite_key, num, counternum, datatype, businesstype
from data.devicemg.device.add import addsite_key, devicetype, num,describe
from data.siteconfig.sitemg.add_site import add_data
addsite_siteType,\
addsite_sitekey,\
addsite_name,\
addsite_city,\
addsite_cityid,\
addsite_proid,\
addsite_regid,\
addsite_areaid,\
addsite_date,\
addsite_status,\
addsite_area,\
getSites_sitekey,\
getSites_type,\
getSites_name,\
getSingleSite_sitekey,\
edit_areaid,edit_cityid,\
edit_proid,edit_regid,\
edit_area,edit_city,\
edit_date,edit_status,\
edit_name=add_data()




class Test_relation(unittest.TestCase):
    def setUp(self):
        SiteMg().addsite(addsite_sitekey,addsite_siteType,addsite_date,addsite_name,addsite_city,addsite_regid,addsite_proid,addsite_cityid,addsite_areaid,addsite_status,addsite_area)
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
        devicekey = Devicemg().getDeviceList(addsite_key).json()['msg']['data'][0]['deviceKey']
        res = Devicemg().getSingleDeviceList(devicekey).json()['msg']
        Devicemg().editDevice(devicekey, res['hostName'], res['deviceId'], res['createTime'], res['modifyTime'], 0,
                              detail=describe, camerakey=camearkey, relationcamera=camearkey)

    def tearDown(self):
        Camera().deleteCamera(camearkey)
        devicekey = Devicemg().getDeviceList(addsite_key).json()['msg']['data'][0]['deviceKey']
        res = Devicemg().getSingleDeviceList(devicekey).json()['msg']
        Devicemg().editDevice(devicekey, res['hostName'], res['deviceId'], res['createTime'], res['modifyTime'], 0,
                              res['detail'])  # 修改设备使能
        result = Devicemg().deleteDevice(devicekey)
        SiteMg().deleteSite(addsite_key)


    def test_relation(self):
        ''' 设备管理-设备绑定摄像头'''
        devicekey = Devicemg().getDeviceList(addsite_key).json()['msg']['data'][0]['deviceKey']
        res = Devicemg().getSingleDeviceList(devicekey).json()['msg']
        result=Devicemg().editDevice(devicekey, res['hostName'], res['deviceId'], res['createTime'], res['modifyTime'], 0,
                              detail=describe,camerakey=camearkey,relationcamera=camearkey).json()['msg']['name']
        self.assertEqual(result, 'Common_Success')






if __name__ == '__main__':
    unittest.main()

