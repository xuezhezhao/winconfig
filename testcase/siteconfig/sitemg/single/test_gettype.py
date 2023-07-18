import pytest
from common.route import *
from api.login.login import Login
from api.siteconfig.sitemg.site_mg import SiteMg

case_data=getType['case_data']

class Test_getType():
    @pytest.mark.parametrize("case_data", case_data,ids=[case_data[i]['case_name'] for i in range(len(case_data))])
    def test_getType(self,case_data):
        case_body=case_data['body']
        except_res=case_data['expect']
        res=SiteMg().getType(sitetype=case_body['siteType']).json()['msg']
        assert res==except_res['msg']


if __name__=='__main__':
    pytest.main()







