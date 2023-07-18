import pytest
from common.route import *
from api.login.login import Login
from api.siteconfig.sitemg.site_mg import SiteMg
from common.regular_control import regular

case_data=deletesite['case_data']

class Test_GetSites():
    @pytest.mark.parametrize("case_data", case_data,ids=[case_data[i]['case_name'] for i in range(len(case_data))])
    def test_getsites(self,case_data):
        case_body=case_data['body']
        except_res=case_data['expect']
        res=SiteMg().deleteSite(sitekey=regular(case_body['siteKey'])).json()['description']
        assert res==except_res['description']


if __name__=='__main__':
    pytest.main()







