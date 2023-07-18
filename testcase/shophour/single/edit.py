import unittest

from api.siteconfig.sitemg.site_mg import SiteMg
from api.siteconfig.shophour.shophour import ShopHour
from data.siteconfig.shophour.shophour import addshophour_type, addshophour_name, addshophour_sitekey, \
    addshophour_isCrossDays, addshophour_enddate, addshophour_begindate, addshophour_endtime, addshophour_begintime, \
    SearchShopHour_sitekey, SearchShopHour_type, editShopHour_type, editShopHour_begindate, editShopHour_enddate, \
    editShopHour_begintime, editShopHour_sitekey, editShopHour_name, editShopHour_endtime, editShopHour_isCrossDays


class Site(unittest.TestCase):
    def setUp(self):
        ShopHour().addShopHour(addshophour_sitekey, addshophour_type, addshophour_begindate, addshophour_enddate,
                                     addshophour_name, addshophour_begintime, addshophour_endtime,
                                     addshophour_isCrossDays)

    def tearDown(self):
        delete_id= ShopHour().SearchShopHour(editShopHour_sitekey, editShopHour_type).json()['msg']['data'][0]['id']
        ShopHour().deleteShopHour(delete_id)

    def test_editShopHour(self):
        '''修改营业时间'''
        id = ShopHour().SearchShopHour(addshophour_sitekey, addshophour_type).json()['msg']['data'][0]['id']
        res = ShopHour().editShopHour(id,editShopHour_sitekey,editShopHour_type,editShopHour_begindate,
                                      editShopHour_enddate,editShopHour_name,editShopHour_begintime,
                                      editShopHour_endtime,editShopHour_isCrossDays).json()
        self.assertEqual(res['description'],'success')



if __name__ == '__main__':
    unittest.main()

