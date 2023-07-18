from api.siteconfig.sitemg.site_mg import SiteMg
from api.devicemg.camera.camera import Camera
import random


# ---- 新增虚拟探头----
root_sitekey = SiteMg().getUserSite().json()['msg'][0]['id']  # 获取根节点sitekey
addsite_key=SiteMg().getNewsitekey(root_sitekey,'300').json()['msg']     #获取添加店铺sitekey
num=1
counternum_list=range(1,9)
counternum=random.choice(counternum_list)
datatype_list=['1B','3A','5B','8B']
datatype=random.choice(datatype_list)
businesstype_list=['1','2','3','6']
businesstype=random.choice(businesstype_list)


 # ---- 新增摄像头----
