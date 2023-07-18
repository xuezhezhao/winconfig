import unittest
# from public.base_request import BaseRequest
# from commn.read import read_excel
from api.siteconfig.sitemg.site_mg import SiteMg
from api.devicemg.camera.camera import Camera
from data.devicemg.camera.add import addsite_key,num,cameraalias
from data.siteconfig.sitemg.add_site import addsite_siteType,addsite_sitekey,addsite_name,addsite_city,addsite_cityid,addsite_proid,addsite_regid,addsite_areaid,addsite_date,addsite_status,addsite_area


file_path=r'C:\Users\admin\Desktop\winconfig接口自动化测试数据.xlsx'
# file_path=r'C:\Users\admin\Desktop\test.xlsx'


class add(unittest.TestCase):
    def setUp(self):
        SiteMg().addsite(addsite_sitekey,addsite_siteType,addsite_date,addsite_name,addsite_city,addsite_regid,addsite_proid,addsite_cityid,addsite_areaid,addsite_status,addsite_area)
    def tearDown(self):
        SiteMg().deleteSite(addsite_key)


    def test_addCamera(self):
        ''' 查看-新增摄像头-查看-编辑-查看-删除-查看'''
        res=Camera().searchCamera(addsite_key).json()['msg']['data']
        self.assertEqual(res,[])
        Camera().addCamera(addsite_key,num)
        camerakey = Camera().searchCamera(addsite_key).json()['msg']['data'][0]['cameraKey']
        cameraname=Camera().searchCamera(addsite_key).json()['msg']['data'][0]['cameraName']
        res=Camera().searchCamera(addsite_key).json()['msg']['data'][0]
        self.assertIn(addsite_key,res['cameraKey'])
        self.assertIn(addsite_key,res['cameraKeyAlias'])
        self.assertEqual(res['cameraName'],'C00001')
        Camera().editCamera(camerakey,cameraname,cameraalias,addsite_key)
        res=Camera().searchCamera(addsite_key).json()['msg']['data'][0]
        self.assertEqual(res['cameraKeyAlias'],cameraalias)
        Camera().deleteCamera(camerakey)
        res=Camera().searchCamera(addsite_key).json()['msg']['data']
        self.assertEqual(res,[])

if __name__=='__main__':
    unittest.main()

