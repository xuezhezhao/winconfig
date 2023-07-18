import unittest
# from public.base_request import BaseRequest
# from commn.read import read_excel
from api.siteconfig.sitemg.site_mg import SiteMg
from data.siteconfig.sitemg.getdata import getType_sitetype,getNewSiteKey_sitetype,getNewSiteKey_sitekey,getHistory_sitekey
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
    @classmethod
    def setUpClass(cls):

        SiteMg().addsite(addsite_sitekey,addsite_siteType,addsite_date,addsite_name,addsite_city,addsite_regid,addsite_proid,addsite_cityid,addsite_areaid,addsite_status,addsite_area)

    @classmethod
    def tearDownClass(cls):
        SiteMg().deleteSite(addsite_sitekey)

    # def test_getType(self):
    #     ''' 场所管理-获取类型'''
    #     res = SiteMg().getType(getType_sitetype).json()
    #     if getType_sitetype=='300':
    #         self.assertEqual(res,{"code":"0","description":"成功","msg":[{"siteTypeCode":400,"siteTypeName":"区域"},{"siteTypeCode":401,"siteTypeName":"店内区域-收银区"},{"siteTypeCode":402,"siteTypeName":"店内区域-揽客区"},{"siteTypeCode":403,"siteTypeName":"店内区域-陪同区"},{"siteTypeCode":404,"siteTypeName":"店内区域-门区"},{"siteTypeCode":500,"siteTypeName":"楼层"},{"siteTypeCode":700,"siteTypeName":"通道"}]})
    #     elif getType_sitetype=='201':
    #         self.assertEqual(res,{"code":"0","description":"成功","msg":[{"siteTypeCode":201,"siteTypeName":"经销商"},{"siteTypeCode":202,"siteTypeName":"事业部"},{"siteTypeCode":203,"siteTypeName":"品牌"},{"siteTypeCode":204,"siteTypeName":"区域"},{"siteTypeCode":205,"siteTypeName":"省份"},{"siteTypeCode":206,"siteTypeName":"城市"},{"siteTypeCode":210,"siteTypeName":"经销商分类"},{"siteTypeCode":300,"siteTypeName":"店铺"}]})
    #     elif getType_sitetype=='202':
    #         self.assertEqual(res,{"code":"0","description":"成功","msg":[{"siteTypeCode":202,"siteTypeName":"事业部"},{"siteTypeCode":203,"siteTypeName":"品牌"},{"siteTypeCode":204,"siteTypeName":"区域"},{"siteTypeCode":205,"siteTypeName":"省份"},{"siteTypeCode":206,"siteTypeName":"城市"},{"siteTypeCode":210,"siteTypeName":"经销商分类"},{"siteTypeCode":300,"siteTypeName":"店铺"}]})
    #     elif getType_sitetype=='203':
    #         self.assertEqual(res,{"code":"0","description":"成功","msg":[{"siteTypeCode":203,"siteTypeName":"品牌"},{"siteTypeCode":204,"siteTypeName":"区域"},{"siteTypeCode":205,"siteTypeName":"省份"},{"siteTypeCode":206,"siteTypeName":"城市"},{"siteTypeCode":210,"siteTypeName":"经销商分类"},{"siteTypeCode":300,"siteTypeName":"店铺"}]})
    #     elif getType_sitetype=='204':
    #         self.assertEqual(res,{"code":"0","description":"成功","msg":[{"siteTypeCode":204,"siteTypeName":"区域"},{"siteTypeCode":205,"siteTypeName":"省份"},{"siteTypeCode":206,"siteTypeName":"城市"},{"siteTypeCode":210,"siteTypeName":"经销商分类"},{"siteTypeCode":300,"siteTypeName":"店铺"}]})
    #     elif getType_sitetype=='205':
    #         self.assertEqual(res,{"code":"0","description":"成功","msg":[{"siteTypeCode":205,"siteTypeName":"省份"},{"siteTypeCode":206,"siteTypeName":"城市"},{"siteTypeCode":210,"siteTypeName":"经销商分类"},{"siteTypeCode":300,"siteTypeName":"店铺"}]})
    #     elif getType_sitetype=='206':
    #         self.assertEqual(res,{"code":"0","description":"成功","msg":[{"siteTypeCode":206,"siteTypeName":"城市"},{"siteTypeCode":210,"siteTypeName":"经销商分类"},{"siteTypeCode":300,"siteTypeName":"店铺"}]})
    #     elif getType_sitetype=='207' or '210':
    #         self.assertEqual(res,{"code":"0","description":"成功","msg":[{"siteTypeCode":210,"siteTypeName":"经销商分类"},{"siteTypeCode":300,"siteTypeName":"店铺"}]})
    #     else:
    #         self.assertEqual(res,{"code":"0","description":"成功","msg":[{"siteTypeCode":200,"siteTypeName":"地域"},{"siteTypeCode":201,"siteTypeName":"经销商"},{"siteTypeCode":202,"siteTypeName":"事业部"},{"siteTypeCode":203,"siteTypeName":"品牌"},{"siteTypeCode":204,"siteTypeName":"区域"},{"siteTypeCode":205,"siteTypeName":"省份"},{"siteTypeCode":206,"siteTypeName":"城市"},{"siteTypeCode":210,"siteTypeName":"经销商分类"},{"siteTypeCode":300,"siteTypeName":"店铺"}]})

    def test_getStatus(self):
        ''' 场所管理-获取场所状态'''
        res=SiteMg().getStatus().json()
        self.assertEqual(res,{"code":"0","description":"成功","msg":[{"siteStatusCode":1,"siteStatusName":"运行"},{"siteStatusCode":2,"siteStatusName":"暂停"},{"siteStatusCode":3,"siteStatusName":"关闭"}]})


    def test_getNewsitekey(self):
        ''' 场所管理-获取新建场所sitekey'''
        res=SiteMg().getNewsitekey(getNewSiteKey_sitekey,getNewSiteKey_sitetype).json()['description']
        self.assertEqual(res,'成功')


    def test_getHistory(self):
        ''' 场所管理-历史查询'''
        res = SiteMg().getHistory(getHistory_sitekey).json()['description']
        self.assertEqual(res, '成功')


    def test_getSiteCamera(self):
        ''' 场所管理-查看场所下摄像头'''
        res = SiteMg().getSiteCamera(addsite_sitekey).json()['msg']
        self.assertEqual(res, [])


    def test_getRelationCamera(self):
        ''' 场所管理-查看场所下摄像头'''
        res = SiteMg().getRelationCamera(addsite_sitekey).json()['msg']
        self.assertEqual(res, {"totalNum":0,"data":[]})
if __name__=='__main__':
    unittest.main()

