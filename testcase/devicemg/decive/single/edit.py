import unittest
# from public.base_request import BaseRequest
# from commn.read import read_excel
from api.siteconfig.sitemg.site_mg import SiteMg
from api.devicemg.device.device import Devicemg
from data.devicemg.device.add import addsite_key,devicetype,num,describe,hostname

file_path=r'C:\Users\admin\Desktop\winconfig接口自动化测试数据.xlsx'
# file_path=r'C:\Users\admin\Desktop\test.xlsx'


class device(unittest.TestCase):
    def setUp(self):
        SiteMg().addsite(addsite_key, '300', '汇纳一号店铺', 10000, '440300')
        Devicemg().addDevice(addsite_key, devicetype, num)
    def tearDown(self):
        devicekey = Devicemg().getDeviceList(addsite_key).json()['msg']['data'][0]['deviceKey']
        res=Devicemg().getSingleDeviceList(devicekey).json()['msg']
        Devicemg().editDevice(devicekey,res['hostName'],res['deviceId'],res['createTime'],res['modifyTime'],0,res['detail'])   #修改设备使能
        Devicemg().deleteDevice(devicekey)   # 删除设备
        SiteMg().deleteSite(addsite_key)   # 删除场所


    def test_getSiteCamera(self):
        ''' 设备管理-配置设备-查看摄像头'''
        res=Devicemg().getSiteCamera(addsite_key).json()['msg']
        self.assertEqual(res,None)
    def test_getSiteDeviceKeyList(self):
        ''' 设备管理-配置设备-查看设备编码'''
        devicekey=Devicemg().getDeviceList(addsite_key).json()['msg']['data'][0]['deviceKey']
        res=Devicemg().getSiteDeviceKeyList(addsite_key).json()['msg'][0]['deviceKey']
        self.assertEqual(res,devicekey)

    def test_editDeviceHostName(self):
        ''' 设备管理-修改设备点码'''
        devicekey = Devicemg().getDeviceList(addsite_key).json()['msg']['data'][0]['deviceKey']
        res = Devicemg().editDeviceHostName(devicekey,hostname).json()['msg']['name']
        self.assertEqual(res, 'Common_Success')
    def test_editDevice(self):
        ''' 设备管理-编辑设备'''
        devicekey = Devicemg().getDeviceList(addsite_key).json()['msg']['data'][0]['deviceKey']
        res = Devicemg().getSingleDeviceList(devicekey).json()['msg']
        result=Devicemg().editDevice(devicekey, res['hostName'], res['deviceId'], res['createTime'], res['modifyTime'], 0,detail=describe).json()['msg']['name']
        self.assertEqual(result, 'Common_Success')

if __name__=='__main__':
    unittest.main()

