import yaml
from api.login.login import Login
import os

a=Login().login().json()
# 把登录的token写入到token.yaml文件，所有用例只需要登录一次，不用每次登录
def writeToken():
    curPath = os.path.abspath(os.path.dirname(__file__))
    tokenFile = os.path.join(curPath, "token.yaml")
    Authorization = {
        "Authorization": Login().login().headers["Authorization"]
    }
    with open(tokenFile, "w", encoding="utf-8") as f:
        yaml.dump(Authorization, f)
    # print("denglu chengg ")


# 读取token.yaml文件的token，后边直接传入headers
def readToken():
    yaml.warnings({'YAMLLoadWarning': False}) # 处理读取文件报错
    curPath = os.path.abspath(os.path.dirname(__file__))
    tokenFile = os.path.join(curPath, "token.yaml")
    openfile = open(tokenFile)
    readfile = openfile.read()
    content = yaml.load(readfile)
    openfile.close()
    return content["Authorization"]


if __name__ == '__main__':
    writeToken()
