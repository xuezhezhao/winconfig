import configparser
import os,sys

path='C:\\Users\\12097\\OneDrive\\自动化测试\\winconfig（new）\\config\\config.ini'
# rf=configparser.ConfigParser()
# rf.read(path,encoding='utf-8')


class ReadFile:
    def __init__(self):
        self.rf=configparser.ConfigParser()
        self.rf.read(path,encoding='utf-8')
    def get_key(self,sec,opt):
        key=self.rf.get(sec,opt)
        return key

if __name__=='__main__':
    print(ReadFile().get_key('HTTP','url'))
