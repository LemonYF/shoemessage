import http.client
import json
import requests

url = 'https://unite.nike.com/login?appVersion=468&experienceVersion=382&uxid=com.nike.commerce.nikedotcom.web&locale=zh_CN&backendEnvironment=identity&browser=Google%20Inc.&os=undefined&mobile=false&native=false&visit=2&visitor=fe7751d5-63ec-49d4-8b95-f9ad7132e431'
payload = {"username": "919024797@qq.com", "password": "Yf458232", "client_id": "HlHa2Cje3ctlaOqnxvgZXNaAs7T9nAuH",
           "ux_id": "com.nike.commerce.nikedotcom.web", "grant_type": "password"}

pre_login_headers = {
    'Accept-Language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
    'Content-Type': 'application/json',
    'scheme': 'https',
    'access-control-request-headers': "content-type",
    'origin': 'https://www.nike.com',
    'referer': 'https://www.nike.com/cn/zh_cn/e/nike-plus-membership',
    'access-control-request-method': 'POST',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",

}

login_headers = {
    # 'authority': 'unite.nike.com',
    # 'authorization': bearer + token,
    # 'authorization': "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc2YWI1NThkLWMwZTMtNGVhYi05MTljLTJkYjA3YjFjN2NhMHNpZyJ9.eyJpYXQiOjE1MzM5MDI5MDIsImV4cCI6MTUzMzkwNjUwMiwiaXNzIjoib2F1dGgyYWNjIiwianRpIjoiZDcyYjlhZmItZDMxNC00NmVkLWFiYTAtYTM4N2MzMDE0OTRkIiwibGF0IjoxNTMzOTAyOTAyLCJhdWQiOiJjb20ubmlrZS5kaWdpdGFsIiwic3ViIjoiY29tLm5pa2UuY29tbWVyY2UubmlrZWRvdGNvbS53ZWIiLCJzYnQiOiJuaWtlOmFwcCIsInNjcCI6WyJuaWtlLmRpZ2l0YWwiXSwicHJuIjoiMTUzODI2MDI4MjUiLCJwcnQiOiJuaWtlOnBsdXMifQ.TUlu7U57cwdyZ0ltHv1CM1mWLH_CIb-GXPZOYQzeTRQFgugiM2Lnza9D2q3WtAO5XXgYIjPrrViAR_cSRN77CGiSGjg0E6qs_gtqky-GE0BmzEX7F4NjpBPk0DcUe4eIteJWQn_pue0FUGJ-NELgUWca3ud5EX5O9kAcVRvtNBDpL_F8R8wZuz0SxxRdXLJAaiNCAADLkTmm-9tvNoXbOKWNmNBRY_3I4pscozAQiky-DP0GaDLuhE3eyA88IuyXmicvb8SeY8asit1b-MlXnC8bCODLvZvMD2AkjN9cwkcd0wWYBV362Tbu9h2dmb6lxKIAkbwX_K801A1CS-oCjg","refresh_token":"eyJhbGciOiJSUzI1NiIsImtpZCI6IjA3ZmQ4ZGJmLTU3NDktNDlkNC05NDNkLTIzNDIwMmNiYjk3MXNpZyJ9.eyJpYXQiOjE1MzM5MDI5MDIsImV4cCI6MTU2NTQzODkwMiwiaXNzIjoib2F1dGgyaWR0IiwianRpIjoiZDZhZjY2ZmUtMWM4ZC00ZjhmLThhN2MtNWIzN2ZiY2YyNWFlIiwibGF0IjoxNTMzOTAyOTAyLCJhdWQiOiJvYXV0aDJpZHQiLCJjbGkiOiJIbEhhMkNqZTNjdGxhT3FueHZnWlhOYUFzN1Q5bkF1SCIsInN1YiI6IjE1MzgyNjAyODI1Iiwic2J0IjoibmlrZTpwbHVzIn0.cA5Jw8WTbA_sOFFetKMbwGDv2SRmguRv2EHtbMR42sISs8U_djur7tzBKygr2YKBVIxPJGjxfmN8R-hMpr_b1FZd52QwK4CWBc66w-s3Rp5pcFD1vR1wc7Ql3hPQcUIpY8OgMDnxNrVsgcpJAPn34nl4tSsfWGnqdyyzYWe_usxXENsKsjxqSXotKBCjIhoaUsOD_ejHUC5JHbtoYx_ZLZuFomXRanV38RFVaIK6wiOQJf-tPnBXLoNQwBTj-YlRIGKKfaVyW0-pwXvJiOmwjJDPs6H1C5tksw88zE-dLLEtnt9aA2b-tEJuhYZWQEQJQVRoKoJqHqrO0Uvqi6Wx_g",
    # 'cache-control': "no-cache",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    # 'X-NewRelic-ID': "VQYGVF5SCBADUVBRBgAGVg==",
    'Cookie':'AnalysisUserId=60.221.220.86.124161533902879292; anonymousId=EEC72DE834B893828F9078F255115BF1; AKA_A2=A; bm_sz=CC3EEE2F66D033FB4DF2B795EF85459F~QAAQVtzdPMonwNRkAQAAPHq8I7LfzYJloIS6pQfmd3rW4sMsyd/AP+ekwWGquj3ofuV7ao/bxe9V/DXw1LTMnuX+yoe/dKo0DIJuCtHMplLVklbKR5J3UFy96z7gHOjSUtkROx3z2Qls2tPgjG288BJ9Pg0hqgw7+75AoAXf2+33k5j1fa8PjatoXJ4R; nike_locale=cn/zh_cn; NIKE_COMMERCE_COUNTRY=CN; NIKE_COMMERCE_LANG_LOCALE=zh_CN; utag_main=_st:1533904684245$ses_id:1533903275849%3Bexp-session; nike_cp=cnns_aff_020116_a_alwmc_wsty_01; guidU=ecd8210d-7df7-408c-feda-0dae15a54a53; neo.swimlane=50; mm_wc_pmt=1; ph_cookie=1; dreams_sample=13; guidS=347886cd-4f02-43d8-e085-ebf711e6fba8; guidSTimestamp=1533902884968|1533902884968; cicPWIntercept=1; neo.experiments=%7B%22main%22%3A%7B%223333-interceptor-cn-jp%22%3A%22a%22%2C%223698-interceptor%22%3A%22a%22%7D%7D; AMCVS_F0935E09512D2C270A490D4D%40AdobeOrg=1; bm_sv=5D47DCCE0069447D19E665BC776EA973~XKqut59jFJ/6Jhsmg7U1Z73qZjFIn2dN3KK5n+KtjcT2+SToKqhk6hqkAmhQD7Roh7Onij3qa4yskym+0l1X+ySKVE41ZS1I4Xk0ww7xWxi+RfOxV7C0jskoxLSmdEqsFom+wZLKcUTheg1Oh1Hu9w==; ak_bmsc=0490E4ED0D11AAED7E15C8733EC5D8D73CDDDC56803000001F806D5B7ACEF70A~plu4t1liVx6edk4IpeYdj8wWJFiPOKycWyTUo9Otex6a2aVJQGUSUqy1HsS0T6yhQsmhFgj+1+IJdPAGvF4qM6ISvehZvXm0AKfCIM/mxNVtuIzzad72TGUfq60N3pW5vHddlYjHK3FvKgA/PkmRumZ6vY7mvM8KAwqJNrhLCW4/4z5xzdw5espjgFH3QRdrWBJQinZXVC3PZ7l+mjt5zawAIAtpNj8EjBVdx+qT3sjGVx9GDR0/3BFaLG0gx8ube+; exp.swoosh.user=%7B%22granted%22%3A0%7D; RES_TRACKINGID=758353544143394; ResonanceSegment=1; RES_SESSIONID=127426904953169; AMCV_F0935E09512D2C270A490D4D%40AdobeOrg=2121618341%7CMCIDTS%7C17754%7CMCMID%7C78110942509688735383068590327086701363%7CMCAAMLH-1534507685%7C11%7CMCAAMB-1534507685%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1533910085s%7CNONE%7CMCAID%7CNONE; ppd=homepage%7Cnikecom%3Estore%20homepage; s_sess=%20c51%3Dhorizontal%3B%20s_cc%3Dtrue%3B%20prevList2%3D%3B; _gscu_207448657=33902886yz9mn581; _gscbrs_207448657=1; _gscs_207448657=33902886yu2eqa81|pv:1; _smt_uid=5b6d8026.92df82c; _abck=0BFAE2CC8935844C994DD762B4B1F4133CDDDC56803000001F806D5B772D3309~0~lWiRgugjUyJL/cfLSQSOWCxInvZnE4IG/yYKgogxzy4=~-1~-1; ajs_user_id=null; ajs_group_id=null; RT="sl=1&ss=1533902879095&tt=7470&obo=0&bcn=%2F%2F36fb68c2.akstat.io%2F&sh=1533902886572%3D1%3A0%3A7470&dm=nike.com&si=f34c793d-40c7-457e-944d-d47762580c94&ld=1533902886572&nu=&cl=1533902901613"; s_pers=%20s_dfa%3Dnikecomprod%7C1533904684602%3B%20c58%3Dno%2520value%7C1533904705601%3B',
    'Accept-Language': "zh-Hans-CN;q=1, en-CN;q=0.9",
    'Content-Type': "application/json",
    'scheme': 'https',
    'origin': 'https://www.nike.com',
    'referer': 'https://www.nike.com/cn/zh_cn/e/nike-plus-membership'
    }

def login(url, payload, login_headers):
    res = requests.post(url, data=json.dumps(payload), headers=login_headers)
    return res

def pre_login(url, pre_login_headers):
    res = requests.options(url, headers = pre_login_headers)
    print('\n', res.headers['Set-Cookie'])
    return res

def start():
    r = pre_login(url, pre_login_headers)
    if (r.status_code==200):
        login_headers['Cookie']= r.headers['Set-Cookie']
        print('\n', login_headers['Cookie'])
        res = login(url, payload, login_headers)
    print('\n', res.content)
    # return res.content

# login?appVersion=468&experienceVersion=382&uxid=com.nike.commerce.nikedotcom.web&locale=zh_CN&backendEnvironment=identity&browser=Google%20Inc.&os=undefined&mobile=false&native=false&visit=2&visitor=fe7751d5-63ec-49d4-8b95-f9ad7132e431
# conn = http.client.HTTPSConnection("unite.nike.com")
# bearer = "Bearer "
# token = "222"
# payload = {"username":"919024797@qq.com","password":"Yf458232","client_id":"HlHa2Cje3ctlaOqnxvgZXNaAs7T9nAuH","ux_id":"com.nike.commerce.nikedotcom.web","grant_type":"password"}
#
#
#
#
#
# r = requests.post(url, data=json.dumps(payload), headers=login_headers)

# conn.request("POST", "login?appVersion=468&experienceVersion=382&uxid=com.nike.commerce.nikedotcom.web&locale=zh_CN&backendEnvironment=identity&browser=Google%20Inc.&os=undefined&mobile=false&native=false&visit=2&visitor=fe7751d5-63ec-49d4-8b95-f9ad7132e431", data=json.dumps(payload), headers=headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))
# print(r.content.decode())
#print(headers["authorization"])
start()
# pre_login(url, pre_login_headers)