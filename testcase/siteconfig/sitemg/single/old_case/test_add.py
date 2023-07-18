import unittest
# from public.base_request import BaseRequest
# from commn.read import read_excel
from api.siteconfig.sitemg.site_mg import SiteMg
from data.siteconfig.sitemg.add_site import add_data
import pytest


addsite_siteType,addsite_sitekey,addsite_name,addsite_city,addsite_cityid,addsite_proid,addsite_regid,addsite_areaid,addsite_date,addsite_status,addsite_area,getSites_sitekey,getSites_type,getSites_name,getSingleSite_sitekey,edit_areaid,edit_cityid,edit_proid,edit_regid,edit_area,edit_city,edit_date,edit_status,edit_name=add_data()


class Test_Site(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        SiteMg().deleteSite(addsite_sitekey)
    def test_addsite(self):
        ''' 场所管理-新建场所'''

        res=SiteMg().addsite(addsite_sitekey,addsite_siteType,addsite_date,addsite_name,addsite_city,addsite_regid,addsite_proid,addsite_cityid,addsite_areaid,addsite_status,addsite_area).json()['msg']
        self.assertEqual('成功',res)


if __name__=='__main__':
    unittest.main()


