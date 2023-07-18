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

        SiteMg().addsite(addsite_key, '300',"2022-09-22",'汇纳一号广场','540400',100000,4,540000,540400,540424,5000 )
    def tearDown(self):
        camearkey=Camera().searchCamera(addsite_key).json()['msg']['data'][0]['cameraKey']
        Camera().deleteCamera(camearkey)
        SiteMg().deleteSite(addsite_key)


    def test_addCamera(self):
        ''' 设备管理-新增摄像头'''
        res=Camera().addCamera(addsite_key,num).json()['description']
        self.assertEqual(res,'数据保存成功')

if __name__=='__main__':
    unittest.main()

