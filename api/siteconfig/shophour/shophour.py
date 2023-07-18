import requests
import json
import urllib3
from api.login.login import Login
urllib3.disable_warnings()
from common.readconfig import ReadFile
from common.writetoken import readToken

host=ReadFile().get_key('HTTP','url')+':'+ReadFile().get_key('HTTP','port')
class ShopHour():
    def addShopHour(self,sitekey,type,begindate,endate,name,begintime,endtime,crossday):  # 添加营业时间
        url = host+'/api/zh-cn/ShopHour/addShopHour'
        data = {"menuId":"1000203",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "Params":{"siteKey":sitekey,
                          "period":type,
                          "beginDate":begindate,
                          "endDate":endate,
                          "name":name,
                          "beginTime":begintime,
                          "endTime":endtime,
                          "isCrossDays":crossday,
                          "monday":1,
                          "tuesday":1,
                          "wednesday":1,
                          "thursday":1,
                          "friday":1,
                          "saturday":1,
                          "sunday":1
                          }
                }
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = readToken()
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def SearchShopHour(self, sitekey,type):  # 查询场所营业时间
        url = host+'/api/zh-cn/ShopHour/SearchShopHour'
        data = {"menuId":"1000203",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "params":{"SiteKey":sitekey,
                          "Period":type,
                          "PageIndex":1,
                          "PageSize":10}
                }
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = readToken()
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def editShopHour(self,id,sitekey,type,begindate,endate,name,begintime,endtime,crossday):  # 编辑营业时间
        url = host+'/api/zh-cn/ShopHour/editShopHour'
        data = {"menuId":"1000203",
                "userId":Login().get_userid(),
                "Params":{"id":id,
                          "siteKey":sitekey,
                          "period":type,
                          "beginDate":begindate,
                          "endDate":endate,
                          "name":name,
                          "beginTime":begintime,
                          "endTime":endtime,
                          "isCrossDays":crossday,
                          "monday":1,
                          "tuesday":1,
                          "wednesday":1,
                          "thursday":1,
                          "friday":1,
                          "saturday":1,
                          "sunday":1}
                }
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = readToken()
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def deleteShopHour(self,id):  # 删除营业时间
        url = host+'/api/zh-cn/ShopHour/deleteShopHour'
        data = {"menuId":"1000203",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "Params":{"id":id}
                }
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = Login().get_cookie()
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result
    def searchHisShopHour(self,id):  # 查看历史营业时间
        url = host+'/api/zh-cn/ShopHour/searchHisShopHour'
        data = {"menuId":"1000203",
                "userId":Login().get_userid(),
                "lang":"zh-cn",
                "Params":{"id":id,
                          "PageIndex":1,
                          "PageSize":10}
                }
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = readToken()
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return result


if __name__=='__main__':
    pass

