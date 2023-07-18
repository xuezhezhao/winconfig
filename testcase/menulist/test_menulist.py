import pytest
from common.route import *
from api.login.login import Login
from api.menulist.menulisg import MenuList

case_data=getUserMenuList['case_data']


class Test_getUserMenuList():
    @pytest.mark.parametrize("case_data", case_data,ids=[case_data[i]['case_name'] for i in range(len(case_data))])
    def test_getUserMenuList(self,case_data):
        case_body=case_data['body']
        except_res=case_data['expect']
        res=MenuList().getUserMenuList(source=case_body["source"]).json()['description']
        assert res==except_res['description']


if __name__=='__main__':
    pytest.main()







