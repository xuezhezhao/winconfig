import pytest
from common.route import *
from api.login.login import Login
from api.siteconfig.sitemg.site_mg import SiteMg

case_data=getstatus['case_data']

class Test_GetStatus():
    @pytest.mark.parametrize("case_data", case_data,ids=[case_data[i]['case_name'] for i in range(len(case_data))])
    def test_getstatus(self,case_data):
        case_body=case_data['body']
        except_res=case_data['expect']
        res=SiteMg().getStatus(status=case_body['siteStatus']).json()['description']
        assert res==except_res['description']


if __name__=='__main__':
    pytest.main()







