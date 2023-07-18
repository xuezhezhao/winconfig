import unittest
from api.siteconfig.sitemg.site_mg import SiteMg
from api.siteconfig.shophour.shophour import ShopHour
from data.siteconfig.shophour.shophour import addshophour_type, addshophour_name, addshophour_sitekey, \
    addshophour_isCrossDays, addshophour_enddate, addshophour_begindate, addshophour_endtime, addshophour_begintime, \
    SearchShopHour_sitekey, SearchShopHour_type, editShopHour_type, editShopHour_begindate, editShopHour_enddate, \
    editShopHour_begintime, editShopHour_sitekey, editShopHour_name, editShopHour_endtime, editShopHour_isCrossDays


class Site(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        id=ShopHour().SearchShopHour(addshophour_sitekey,addshophour_type).json()['msg']['data'][0]['id']
        ShopHour().deleteShopHour(id)

    def test_addshophour(self):
        '''添加营业时间'''
        res = ShopHour().addShopHour(addshophour_sitekey, addshophour_type, addshophour_begindate, addshophour_enddate,
                                     addshophour_name, addshophour_begintime, addshophour_endtime,
                                     addshophour_isCrossDays).json()['description']
        self.assertEqual(res, '成功')


if __name__ == '__main__':
    unittest.main()

