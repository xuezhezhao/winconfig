import unittest
# from public.base_request import BaseRequest
# from commn.read import read_excel
from api.siteconfig.sitemg.site_mg import SiteMg
from api.devicemg.camera.camera import Camera
from data.devicemg.camera.add import addsite_key,num

file_path=r'C:\Users\admin\Desktop\winconfig接口自动化测试数据.xlsx'
# file_path=r'C:\Users\admin\Desktop\test.xlsx'


class add(unittest.TestCase):
    def setUp(self):

        SiteMg().addsite(addsite_key, '300', '汇纳一号店铺', 10000, '440300')
        Camera().addCamera(addsite_key, num)
        global camearkey
        camearkey = Camera().searchCamera(addsite_key).json()['msg']['data'][0]['cameraKey']
    def tearDown(self):
        SiteMg().deleteSite(addsite_key)

    def test_deleteCamera(self):
        ''' 设备管理-删除摄像头'''
        res=Camera().deleteCamera(camearkey).json()['description']
        self.assertEqual(res,'删除成功！')

if __name__=='__main__':
    unittest.main()

