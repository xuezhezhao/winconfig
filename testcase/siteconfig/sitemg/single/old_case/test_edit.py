import unittest
# from public.base_request import BaseRequest
# from commn.read import read_excel
from api.siteconfig.sitemg.site_mg import SiteMg
from data.siteconfig.sitemg.add_site import add_data
addsite_siteType,\
addsite_sitekey,\
addsite_name,\
addsite_city,\
addsite_cityid,\
addsite_proid,\
addsite_regid,\
addsite_areaid,\
addsite_date,\
addsite_status,\
addsite_area,\
getSites_sitekey,\
getSites_type,\
getSites_name,\
getSingleSite_sitekey,\
edit_areaid,edit_cityid,\
edit_proid,edit_regid,\
edit_area,edit_city,\
edit_date,edit_status,\
edit_name=add_data()



class Test_Site(unittest.TestCase):
    def setUp(self):

        SiteMg().addsite(addsite_sitekey,addsite_siteType,addsite_date,addsite_name,addsite_city,addsite_regid,addsite_proid,addsite_cityid,addsite_areaid,addsite_status,addsite_area)

    def tearDown(self):
        SiteMg().deleteSite(addsite_sitekey)

    def test_addsite(self):
        ''' 场所管理-编辑场所'''
        res2 = SiteMg().getSingleSite(getSingleSite_sitekey).json()['msg']
        res=SiteMg().editSite(addsite_sitekey,addsite_siteType,edit_date,edit_name,edit_city,edit_regid,edit_proid,edit_cityid,edit_areaid,edit_area).json()['msg']
        self.assertEqual(res,'成功')

if __name__=='__main__':
    unittest.main()

