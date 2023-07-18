import unittest
# from public.base_request import BaseRequest
# from commn.read import read_excel
from api.siteconfig.sitemg.site_mg import SiteMg
from api.devicemg.device.device import Devicemg
from data.devicemg.device.add import addsite_key,devicetype,num

file_path=r'C:\Users\admin\Desktop\winconfig接口自动化测试数据.xlsx'
# file_path=r'C:\Users\admin\Desktop\test.xlsx'


class device(unittest.TestCase):
    def setUp(self):
        SiteMg().addsite(addsite_key, '300', '汇纳一号店铺', 10000, '440300')
        Devicemg().addDevice(addsite_key, devicetype, num)
    def tearDown(self):
        SiteMg().deleteSite(addsite_key)


    def test_searchdevice(self):
        ''' 设备管理-查找设备'''
        res=Devicemg().getDeviceList(addsite_key).json()['msg']['data'][-1]['deviceType']
        self.assertEqual(res,devicetype)
    def test_getSingleDevice(self):
        ''' 设备管理-查看设备'''
        devicekey=Devicemg().getDeviceList(addsite_key).json()['msg']['data'][-1]['deviceKey']
        res=Devicemg().getSingleDeviceList(devicekey).json()['msg']['deviceKey']
        self.assertEqual(res,devicekey)

if __name__=='__main__':
    unittest.main()

