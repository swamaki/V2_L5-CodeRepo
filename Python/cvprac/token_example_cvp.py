#!/usr/bin/env python3

from cvprac.cvp_client import CvpClient
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()

cvp1 = "10.18.170.194"  # ACT instance

cvp_user = "ansible"
cvp_pw = "ansible"


clnt = CvpClient()
clnt.connect([cvp1], cvp_user, cvp_pw)
# clnt.connect(nodes=[cvp1], cvp_user, cvp_pw)
print(clnt.api.get_cvp_info())
