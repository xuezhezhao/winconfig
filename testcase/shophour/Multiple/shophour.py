import unittest

from api.siteconfig.sitemg.site_mg import SiteMg
from api.siteconfig.shophour.shophour import ShopHour
from data.siteconfig.shophour.shophour import addshophour_type,addshophour_name,addshophour_sitekey,addshophour_isCrossDays,addshophour_enddate,addshophour_begindate,addshophour_endtime,addshophour_begintime,SearchShopHour_sitekey,SearchShopHour_type,editShopHour_type,editShopHour_begindate,editShopHour_enddate,editShopHour_begintime,editShopHour_sitekey,editShopHour_name,editShopHour_endtime,editShopHour_isCrossDays

class Site(unittest.TestCase):
    def setUp(self):
        self.allErrors = []

    def tearDown(self):
        self.assertEqual([], self.allErrors)

    def test_addshophour(self):
        res=ShopHour().addShopHour(addshophour_sitekey,addshophour_type,addshophour_begindate,addshophour_enddate,addshophour_name,addshophour_begintime,addshophour_endtime,addshophour_isCrossDays).json()['description']
        self.assertEqual(res,'成功')
        res1=ShopHour().SearchShopHour(SearchShopHour_sitekey,SearchShopHour_type).json()['msg']['data'][0]
        self.assertEqual(res1['siteKey'],addshophour_sitekey)
        self.assertEqual(res1['siteName'],addshophour_name)
        self.assertEqual(res1['beginDate'], addshophour_begindate)
        self.assertEqual(res1['beginTime'], addshophour_begintime)
        self.assertEqual(res1['endDate'], addshophour_enddate)
        self.assertEqual(res1['endTime'], addshophour_endtime)
        id=res1['id']
        res2=ShopHour().editShopHour(id,editShopHour_sitekey,editShopHour_type,editShopHour_begindate,editShopHour_enddate,editShopHour_name,editShopHour_begintime,editShopHour_endtime,editShopHour_isCrossDays).json()
        self.assertEqual(res2['description'],'success')
        res3=ShopHour().SearchShopHour(editShopHour_sitekey,editShopHour_type).json()['msg']['data'][0]
        self.assertEqual(res3['siteKey'], editShopHour_sitekey)
        self.assertEqual(res3['siteName'], editShopHour_name)
        self.assertEqual(res3['beginDate'], editShopHour_begindate)
        self.assertEqual(res3['beginTime'], editShopHour_begintime)
        self.assertEqual(res3['endDate'], editShopHour_enddate)
        self.assertEqual(res3['endTime'], editShopHour_endtime)
        res4=ShopHour().deleteShopHour(id).json()
        self.assertEqual(res4['description'],'成功')



if __name__=='__main__':
    unittest.main()

