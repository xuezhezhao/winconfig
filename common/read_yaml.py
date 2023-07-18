import os
import sys
import yaml


def get_yaml_filepath(filepath=""):
        with open(filepath, "r", encoding="utf-8")as f:
            return yaml.load(f, Loader=yaml.FullLoader)

if __name__ == '__main__':
    a=get_yaml_filepath('C:\\Users\\12097\\OneDrive\\自动化测试\\winconfig（new）\\data\\login\\login.yaml')
    print(a)

