import pytest
from common.route import *
from api.login.login import Login
from api.siteconfig.sitemg.site_mg import SiteMg
from common.regular_control import regular

case_data=addsite['case_data']

class Test_GetSites():
    @pytest.mark.parametrize("case_data", case_data,ids=[case_data[i]['case_name'] for i in range(len(case_data))])
    def test_getsites(self,case_data):
        case_body=case_data['body']
        except_res=case_data['expect']
        res=SiteMg().addsite(sitekey=regular(case_body['siteKey']),sitetype=case_body['siteType'],opendate=regular(case_body['openDate']),name=regular(case_body['siteName']),city=case_body['city'],regid=case_body['Region_Id'],proid=case_body['Province_Id'],cityid=case_body['City_Id'],areaid=case_body['Area_Id'],staus=case_body['siteStatus'],area=case_body['area']).json()['description']
        assert res==except_res['description']


if __name__=='__main__':
    pytest.main()







