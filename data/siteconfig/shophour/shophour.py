#   -----营业时间管理-添加营业时间-------
from api.siteconfig.sitemg.site_mg import SiteMg
import random
res=SiteMg().getUserSite().json()
root_sitekey = SiteMg().getUserSite().json()['msg'][0]['id']
root_name=SiteMg().getUserSite().json()['msg'][0]['label']
addshophour_sitekey=root_sitekey
addshophour_name=root_name
addshophour_type=random.choice([0,1,2])
addshophour_isCrossDays=random.choice([0,1])
if addshophour_isCrossDays == 0:
    addshophour_begintime = '10:00'
    addshophour_endtime = '22:00'
else:
    addshophour_begintime = '12:00'
    addshophour_endtime = '03:00'
if addshophour_type==0 or 1:
    addshophour_begindate='01-01'
    addshophour_enddate='12-31'
else:
    addshophour_begindate = '2022-01-01'
    addshophour_enddate = '2022-12-31'
#   -----营业时间管理-查询营业时间-------

SearchShopHour_sitekey=root_sitekey
SearchShopHour_type=addshophour_type

#   -----营业时间管理-编辑营业时间-------

editShopHour_sitekey=root_sitekey
editShopHour_name=root_name
editShopHour_type=random.choice([0,1,2])
editShopHour_isCrossDays=random.choice([0,1])
if editShopHour_isCrossDays == 0:
    editShopHour_begintime = '10:00'
    editShopHour_endtime = '23:00'
else:
    editShopHour_begintime = '12:00'
    editShopHour_endtime = '04:00'
if editShopHour_type==0 or 1:
    editShopHour_begindate='05-01'
    editShopHour_enddate='11-05'
else:
    editShopHour_begindate = '2022-06-01'
    editShopHour_enddate = '2022-10-05'

