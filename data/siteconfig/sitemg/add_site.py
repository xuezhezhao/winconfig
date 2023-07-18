#   -----场所管理-添加场所测试数据-------
from api.siteconfig.sitemg.site_mg import SiteMg
import random
import datetime

def add_data():
 #   -----场所管理-新增场所测试数据-------
 root_sitekey = SiteMg().getUserSite().json()['msg'][0]['id']  # 获取根节点sitekey
 res = SiteMg().getType(100).json()['msg']  # 获取100场所下类型
 type = []
 for i in res:
  type.append(i['siteTypeCode'])
 # sitekey = SiteMg().getUserSite().json()['msg'][0]['id']
 addsite_siteType = random.choice(type)
 if addsite_siteType == 300:
  addsite_area = 6000
  """随机获取大区，省，市，区县id"""
  res = SiteMg().getPositionInfo(1, 100000).json()['msg']
  res.pop()
  addsite_regid = random.choice(res)['id']
  res1 = SiteMg().getPositionInfo(2, addsite_regid).json()['msg']
  addsite_proid = random.choice(res1)['id']
  res2 = SiteMg().getPositionInfo(3, addsite_proid).json()['msg']
  addsite_cityid = random.choice(res2)['id']
  addsite_city = str(addsite_cityid)
  res3 = SiteMg().getPositionInfo(4, addsite_cityid).json()['msg']
  if res3 == []:
   addsite_areaid = 0
  else:
   addsite_areaid = random.choice(res3)['id']
 else:
  addsite_area = 0
  addsite_city = None
  addsite_regid = 0
  addsite_proid = 0
  addsite_cityid = 0
  addsite_areaid = 0

 addsite_sitekey = SiteMg().getNewsitekey(root_sitekey, addsite_siteType).json()['msg']
 addsite_name = '测试场所' + str(random.randint(0, 20000))
 addsite_date = str(datetime.date.today())
 addsite_status = "1"

 # print(addsite_sitekey,addsite_name,addsite_date,addsite_status)
 #   -----场所管理-查看场所测试数据-------

 getSites_sitekey = root_sitekey
 getSites_name = addsite_name
 getSites_type = addsite_siteType



 #   -----场所管理-查看单个场所测试数据-------
 getSingleSite_sitekey = addsite_sitekey



 #   -----场所管理-编辑场所测试数据-------
 edit_name = '测试场所' + str(random.randint(0, 20000))
 edit_date = str(datetime.date.today())
 edit_status = random.choice(['1', '2', '3'])
 if addsite_siteType == 300:
  edit_area = 300
  """随机获取大区，省，市，区县id"""
  res = SiteMg().getPositionInfo(1, 100000).json()['msg']
  res.pop()
  edit_regid = random.choice(res)['id']
  res1 = SiteMg().getPositionInfo(2, addsite_regid).json()['msg']
  edit_proid = random.choice(res1)['id']
  res2 = SiteMg().getPositionInfo(3, addsite_proid).json()['msg']
  edit_cityid = random.choice(res2)['id']
  edit_city = addsite_cityid
  res3 = SiteMg().getPositionInfo(4, addsite_cityid).json()['msg']
  if res3 == []:
   edit_areaid = 0
  else:
   edit_areaid = random.choice(res3)['id']
 else:
  edit_area = 0
  edit_city = None
  edit_regid = 0
  edit_proid = 0
  edit_cityid = 0
  edit_areaid = 0
 return addsite_siteType,addsite_sitekey,addsite_name,addsite_city,addsite_cityid,addsite_proid,addsite_regid,addsite_areaid,addsite_date,addsite_status,addsite_area,getSites_sitekey,getSites_type,getSites_name,getSingleSite_sitekey,edit_areaid,edit_cityid,edit_proid,edit_regid,edit_area,edit_city,edit_date,edit_status,edit_name


# addsite_siteType,addsite_sitekey,addsite_name,addsite_city,addsite_cityid,addsite_proid,addsite_regid,addsite_areaid,addsite_date,addsite_status,addsite_area,getSites_sitekey,getSites_type,getSites_name,getSingleSite_sitekey,edit_areaid,edit_cityid,edit_proid,edit_regid,edit_area,edit_city,edit_date,edit_status,edit_name=add_data()
# print(add_data()[11],add_data()[12],add_data()[13])
# SiteMg().addsite(addsite_sitekey,addsite_siteType,addsite_date,addsite_name,addsite_city,addsite_regid,addsite_proid,addsite_cityid,addsite_areaid,addsite_status,addsite_area).json()
# #
# # print(res)
# print(getSites_name,getSites_sitekey,getSites_type)
# res1 = SiteMg().getSites(getSites_sitekey, getSites_name, sitetype=getSites_type).json()['msg']
# print(res1)


