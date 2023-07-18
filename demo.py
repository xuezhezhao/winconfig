import pytest
from common.route import *
from api.login.login import Login
from api.siteconfig.sitemg.site_mg import SiteMg
from common.regular_control import regular

from common.writetoken import readToken

a=addsite['case_data'][0]

print(regular((a)['body']['siteType']))

print(readToken())
