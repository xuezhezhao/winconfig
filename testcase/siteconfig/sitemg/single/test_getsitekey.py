import pytest
from common.route import *
from api.login.login import Login
from api.siteconfig.sitemg.site_mg import SiteMg

case_data=getnewsitekey['case_data']

class Test_getNewSiteKey():
    @pytest.mark.parametrize("case_data", case_data,ids=[case_data[i]['case_name'] for i in range(len(case_data))])
    def test_getNewSiteKey(self,case_data):
        case_body=case_data['body']
        except_res=case_data['expect']
        res=SiteMg().getNewsitekey(sitekey=case_body['siteKey'],sitetype=case_body['siteType']).json()['description']
        assert res==except_res['description']


if __name__=='__main__':
    pytest.main()







