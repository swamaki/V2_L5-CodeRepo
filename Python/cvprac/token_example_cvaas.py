#!/usr/bin/env python3

from cvprac.cvp_client import CvpClient
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()


cvp1 = "www.cv-staging.corp.arista.io"  # cvaas instance

# cvp_user = "ansible"
# cvp_pw = "ansible"

# token = "{{lookup('file', '../../../../POC/POC_act/cv/cv_act.tok')}}"
token = "{{lookup('file', '../../../../POC/POC_eve/cv/cvaas.tok')}}"


clnt = CvpClient()
# clnt.connect([cvp1], username="", password="", is_cvaas=True, api_token=token)
clnt.connect(
    nodes=["cvaas"], username="", password="", is_cvaas=True, api_token="user token"
)
print(clnt.api.get_cvp_info())
