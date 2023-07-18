import unittest
# from public.base_request import BaseRequest
# from commn.read import read_excel
from api.siteconfig.sitemg.site_mg import SiteMg
from api.devicemg.device.device import Devicemg
from data.devicemg.device.add import addsite_key,devicetype,num,describe

file_path=r'C:\Users\admin\Desktop\winconfig接口自动化测试数据.xlsx'
# file_path=r'C:\Users\admin\Desktop\test.xlsx'


class device(unittest.TestCase):
    def setUp(self):
        SiteMg().addsite(addsite_key, '300', '汇纳一号店铺', 10000, '440300')
        Devicemg().addDevice(addsite_key, devicetype, num)
        devicekey = Devicemg().getDeviceList(addsite_key).json()['msg']['data'][0]['deviceKey']
        res = Devicemg().getSingleDeviceList(devicekey).json()['msg']
        Devicemg().editDevice(devicekey, res['hostName'], res['deviceId'], res['createTime'], res['modifyTime'], 0,
                              res['detail'])  # 修改设备使能
    def tearDown(self):
        SiteMg().deleteSite(addsite_key)   # 删除场所
    def test_deleteDevice(self):
        ''' 设备管理-删除设备'''
        devicekey = Devicemg().getDeviceList(addsite_key).json()['msg']['data'][0]['deviceKey']
        result=Devicemg().deleteDevice(devicekey).json()['msg']['name'] # 删除设备
        self.assertEqual(result,'Common_Success')

if __name__=='__main__':
    unittest.main()

