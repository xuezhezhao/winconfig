from api.siteconfig.sitemg.site_mg import SiteMg
from api.devicemg.device.device import Devicemg
import random
# ---- 新增摄像头----
root_sitekey = SiteMg().getUserSite().json()['msg'][0]['id']  # 获取根节点sitekey
addsite_key=SiteMg().getNewsitekey(root_sitekey,'300').json()['msg']     #获取添加店铺sitekey
num=1
# ---- 编辑摄像头----
cameraalias='789'


