#   -----场所管理-获取场所类型数据-------
import random
from api.siteconfig.sitemg.site_mg import SiteMg
type=['100','200','201','202','203','204','205','206','210','300']
getType_sitetype=random.choice(type)
#   -----场所管理-获取新建场所sitekey数据-------
root_sitekey = SiteMg().getUserSite().json()['msg'][0]['id']  # 获取根节点sitekey
res=SiteMg().getType(100).json()['msg']
type=[]
for i in res:
 type.append(i['siteTypeCode'])
sitekey=SiteMg().getUserSite().json()['msg'][0]['id']
getNewSiteKey_sitekey=root_sitekey
getNewSiteKey_sitetype=random.choice(type)
#   -----场所管理-获取场所历史数据-------
getHistory_sitekey=root_sitekey