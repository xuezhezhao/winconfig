import unittest
# from public.base_request import BaseRequest
# from commn.read import read_excel
from api.siteconfig.sitemg.site_mg import SiteMg
from api.devicemg.device.device import Devicemg
from data.devicemg.device.add import addsite_key,devicetype,num

file_path=r'C:\Users\admin\Desktop\winconfig接口自动化测试数据.xlsx'
# file_path=r'C:\Users\admin\Desktop\test.xlsx'


class add(unittest.TestCase):
    def setUp(self):
        SiteMg().addsite(addsite_key, '300', '汇纳一号店铺', 10000, '440300')
    def tearDown(self):

        SiteMg().deleteSite(addsite_key)


    def test_getSiteCamera(self):
        ''' 设备管理-新增设备-查看场所下摄像头'''
        res = Devicemg().getSiteCamera(addsite_key).json()['msg']
        self.assertEqual(res, None)

    def test_getSiteDeviceKeyList(self):
        ''' 设备管理-查看场所下设备'''
        res = Devicemg().getSiteDeviceKeyList(addsite_key).json()['msg']
        self.assertEqual(res, None)

if __name__=='__main__':
    unittest.main()

