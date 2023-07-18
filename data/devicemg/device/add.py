from api.siteconfig.sitemg.site_mg import SiteMg
from api.devicemg.device.device import Devicemg
import random

#---------添加设备、查看设备-----------
root_sitekey = SiteMg().getUserSite().json()['msg'][0]['id']  # 获取根节点sitekey
addsite_key=SiteMg().getNewsitekey(root_sitekey,'300').json()['msg']     #获取添加店铺sitekey
device_typelist=[]
for a in Devicemg().getDeviceTypeList().json()['msg']:
    device_typelist.append(a['typeName'])
devicetype=random.choice(device_typelist)
num=1

#---------编辑设备-----------
describe='666'
#---------编辑设备点码-----------
hostname='none.ipva.cn123456'
#---------删除设备-----------
