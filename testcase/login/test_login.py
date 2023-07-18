import pytest
from common.route import *
from api.login.login import Login

login_data=login['case_data']

class Test_login():
    @pytest.mark.parametrize("login_data", login_data,ids=[login_data[i]['case_name'] for i in range(len(login_data))])
    def test_login(self,login_data):
        case_body=login_data['body']
        except_res=login_data['expect']
        res=Login().login(user=case_body['UserName'],password=case_body['PassWord']).json()['description']
        assert res==except_res['description']


if __name__=='__main__':
    pytest.main()







