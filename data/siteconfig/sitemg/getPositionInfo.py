from api.siteconfig.sitemg.site_mg import SiteMg
import random

def getposition():
    """随机获取大区，省，市，区县id"""
    #-----获取大区信息---------
    res=SiteMg().getPositionInfo(1,100000).json()['msg']
    res.pop()
    addsite_regid=random.choice(res)['id']
    res1=SiteMg().getPositionInfo(2,addsite_regid).json()['msg']
    addsite_proid=random.choice(res1)['id']
    res2=SiteMg().getPositionInfo(3,addsite_proid).json()['msg']
    addsite_cityid=random.choice(res2)['id']
    res3=SiteMg().getPositionInfo(4,addsite_cityid).json()['msg']
    if res3==[]:
        addsite_areaid=0
    else:
        addsite_areaid = random.choice(res3)['id']
    print(addsite_regid,addsite_proid,addsite_cityid,addsite_areaid)




getposition()