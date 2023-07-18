from unittestreport import TestRunner
# from testcase.login import Test_login
from testcase.siteconfig.sitemg.single.old_case.test_add import Test_Site

import unittest
import os,sys
import time

dirname,filename=os.path.split(os.path.abspath(sys.argv[0]))  #获取该文件的路径及文件名
# print(dirname,filename)
case_path = ".\\case\\"
result = dirname+"\\report\\"

# 创建测试套件
suite = unittest.TestSuite()


loader = unittest.TestLoader()
test_case=['single']
suite.addTest(loader.loadTestsFromTestCase(Test_Site))

# suite.addTests()


now_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# 定义测试报告的存放的路径
path = result + day_time
# 判断路径是否存在
if not os.path.exists(path):
    # 如果不存在，则创建一个
    os.makedirs(path)
else:
    pass
reports_path = path + "\\" + now_time + "（winconfig测试报告）.html"
runner = TestRunner(suite,
                               tester='薛哲曌',
                               filename=now_time + "（winconfig测试报告）.html",
                               report_dir=path + "\\",
                               title='winconfig接口自动化',
                               desc='项目测试生成的报告描述',
                               templates=2
                               )

# 3、运行测试用例
runner.run()
url = "https://oapi.dingtalk.com/robot/send?access_token=9925eb02c1b22baf97eeb6005cd24fc985caa5708ca0b59fb70923ff9fba449d"
# 发送钉钉通知
runner.dingtalk_notice(url=url, key='python')
# 发送邮件通知
# runner.send_email(host=ReadFile().get_key('EMAIL','mail_host'),
#                   port=ReadFile().get_key('EMAIL','port'),
#                   user=ReadFile().get_key('EMAIL','mail_user'),
#                   password=ReadFile().get_key('EMAIL','mail_pass'),
#                   to_addrs=ReadFile().get_key('EMAIL','receivers'))
# send_email(reports_path)


