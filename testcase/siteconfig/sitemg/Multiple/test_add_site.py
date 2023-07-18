import unittest
# from public.base_request import BaseRequest
# from commn.read import read_excel
from api.siteconfig.sitemg.site_mg import SiteMg
from data.siteconfig.sitemg.add_site import add_data
import time



addsite_siteType,addsite_sitekey,addsite_name,addsite_city,addsite_cityid,addsite_proid,addsite_regid,addsite_areaid,addsite_date,addsite_status,addsite_area,getSites_sitekey,getSites_type,getSites_name,getSingleSite_sitekey,edit_areaid,edit_cityid,edit_proid,edit_regid,edit_area,edit_city,edit_date,edit_status,edit_name=add_data()

class Site(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    def test_addsite(self):
        ''' 场所管理-增删改查场所接口用例'''
        res=SiteMg().addsite(addsite_sitekey,addsite_siteType,addsite_date,addsite_name,addsite_city,addsite_regid,addsite_proid,addsite_cityid,addsite_areaid,addsite_status,addsite_area).json()['msg']
        self.assertEqual(res,'成功')
        res1=SiteMg().getSites(getSites_sitekey,getSites_name,sitetype=getSites_type).json()['msg']['data'][0]
        self.assertEqual(res1['siteKey'],addsite_sitekey)
        self.assertEqual(res1['siteName'],addsite_name)
        self.assertEqual(res1['siteType'],addsite_siteType)
        res2=SiteMg().getSingleSite(getSingleSite_sitekey).json()['msg']
        self.assertEqual(res2['area'],addsite_area)
        self.assertEqual(res2['siteKey'],addsite_sitekey)
        self.assertEqual(res2['siteName'],addsite_name)
        self.assertEqual(res2['siteType'],addsite_siteType)
        res3=SiteMg().editSite(addsite_sitekey,addsite_siteType,edit_date,edit_name,edit_city,edit_regid,edit_proid,edit_cityid,edit_areaid,edit_area).json()
        self.assertEqual(res3['msg'],'成功')
        res4 = SiteMg().getSingleSite(getSingleSite_sitekey).json()['msg']
        self.assertEqual(res4['area'], edit_area)
        self.assertEqual(res4['siteName'], edit_name)
        # self.assertEqual(res4['cityId'], int(editsite_city))
        res5=SiteMg().deleteSite(addsite_sitekey).json()
        self.assertEqual(res5['msg'],'成功')
        res6 = SiteMg().getSites(getSites_sitekey,edit_name,sitetype=getSites_type).json()['msg']
        time.sleep(3)
        self.assertTrue(res6['data']==[])
if __name__=='__main__':
    unittest.main()

