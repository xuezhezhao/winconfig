import unittest
from api.siteconfig.sitemg.site_mg import SiteMg
from api.devicemg.device.device import Devicemg
from data.devicemg.device.add import addsite_key,devicetype,num,describe,hostname
class device(unittest.TestCase):
    def setUp(self):
        SiteMg().addsite(addsite_key, '300', '汇纳一号店铺', 10000, '440300')
        self.allErrors = []

    def tearDown(self):
        SiteMg().deleteSite(addsite_key)  # 删除场所
        self.assertEqual([], self.allErrors)

    def test_adddevice(self):
        ''' 查看-添加设备-查看-编辑-查看-删除-查看  '''
        res=Devicemg().getDeviceList(addsite_key).json()['msg']
        self.assertEqual(res,None)
        Devicemg().addDevice(addsite_key, devicetype, num)
        result=Devicemg().getDeviceList(addsite_key).json()['msg']['data'][0]
        self.assertEqual(result['deviceKey'],addsite_key+'TH00001')
        self.assertEqual(result['deviceType'],devicetype)
        Devicemg().editDeviceHostName(result['deviceKey'],hostname)
        res=Devicemg().getDeviceList(addsite_key).json()['msg']['data'][0]
        self.assertEqual(res['hostName'],hostname)
        result1= Devicemg().getSingleDeviceList(result['deviceKey']).json()['msg']
        Devicemg().editDevice(result1['deviceKey'], result1['hostName'], result1['deviceId'], result1['createTime'], result1['modifyTime'], 0,
                              result1['detail'])  # 修改设备使能
        Devicemg().deleteDevice(result1['deviceKey'])
        res=Devicemg().getDeviceList(addsite_key).json()['msg']
        self.assertEqual(res,None)

if __name__=='__main__':
    unittest.main()

