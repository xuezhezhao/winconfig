import unittest
# from public.base_request import BaseRequest
# from commn.read import read_excel
from api.siteconfig.sitemg.site_mg import SiteMg
from api.devicemg.camera.camera import Camera
from data.devicemg.VirCamera.add import addsite_key,num,counternum,datatype,businesstype


file_path=r'C:\Users\admin\Desktop\winconfig接口自动化测试数据.xlsx'
# file_path=r'C:\Users\admin\Desktop\test.xlsx'


class add(unittest.TestCase):
    def setUp(self):
        SiteMg().addsite(addsite_key, '300', '汇纳一号店铺', 10000, '440300')
        Camera().addCamera(addsite_key, num)
        global camearkey
        camearkey = Camera().searchCamera(addsite_key).json()['msg']['data'][0]['cameraKey']
        cameraname = Camera().searchCamera(addsite_key).json()['msg']['data'][0]['cameraName']
        a = camearkey[1:6]
        b = 0
        for c in a:
            if c != '0':
                break
            else:
                b = b + 1
        x = a[b:len(a)]
        d = cameraname[1:6]
        e = 0
        for f in d:
            if f != '0':
                break
            else:
                e = e + 1
        y = d[e:len(d)]
        global virnumber
        virnumber = camearkey[0]+a[b:len(a)] +cameraname[0]+ d[e:len(d)] + '_' + str(counternum) + datatype
        Camera().addVirCameraLs(camearkey, str(counternum), datatype, virnumber, businesstype)
    def tearDown(self):
        Camera().deleteCamera(camearkey)
        SiteMg().deleteSite(addsite_key)


    def test_relationVirCamera(self):
        ''' 设备管理-设备关联摄像头'''


if __name__=='__main__':
    unittest.main()

