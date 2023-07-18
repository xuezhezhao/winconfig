import unittest
# from public.base_request import BaseRequest
# from commn.read import read_excel
from api.siteconfig.sitemg.site_mg import SiteMg
from api.devicemg.camera.camera import Camera
from data.devicemg.camera.add import addsite_key,num,cameraalias

file_path=r'C:\Users\admin\Desktop\winconfig接口自动化测试数据.xlsx'
# file_path=r'C:\Users\admin\Desktop\test.xlsx'


class add(unittest.TestCase):
    def setUp(self):
        SiteMg().addsite(addsite_key, '300', '汇纳一号店铺', 10000, '440300')
        Camera().addCamera(addsite_key, num)
        global camerakey, cameraname
        camerakey = Camera().searchCamera(addsite_key).json()['msg']['data'][0]['cameraKey']
        cameraname=Camera().searchCamera(addsite_key).json()['msg']['data'][0]['cameraName']
    def tearDown(self):
        Camera().deleteCamera(camerakey)
        SiteMg().deleteSite(addsite_key)


    def test_editCamera(self):
        ''' 设备管理-编辑摄像头'''
        res=Camera().editCamera(camerakey,cameraname,cameraalias,addsite_key).json()['description']
        self.assertEqual(res,'数据保存成功')

if __name__=='__main__':
    unittest.main()

