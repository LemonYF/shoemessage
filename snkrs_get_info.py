#!/usr/bin/python
# encoding=utf-8
import requests

def get_shoe_info():
    global res1
    url = 'https://api.nike.com/snkrs/content/v1/?&country=CN&language=zh-Hans&offset=0&orderBy=published'
    try:
        res1 = requests.get(url)
        res1.encoding = 'utf-8'
    except:
        print('warning')
    # print(res1.content)
    return res1






# get_shoe_info()
# headers = {
#         # 'authorization': bearer + token,
#         'authorization': "eyJhbGciOiJSUzI1NiIsImtpZCI6IjA3ZmQ4ZGJmLTU3NDktNDlkNC05NDNkLTIzNDIwMmNiYjk3MXNpZyJ9.eyJpYXQiOjE1MzM5MjA4MjMsImV4cCI6MTU2NTQ1NjgyMywiaXNzIjoib2F1dGgyaWR0IiwianRpIjoiOGRhYTU4ZjAtNDAzOC00ZDIxLWIwYzgtNTNiMmU1NzJkYzRkIiwibGF0IjoxNTMzOTIwODIzLCJhdWQiOiJvYXV0aDJpZHQiLCJjbGkiOiJIbEhhMkNqZTNjdGxhT3FueHZnWlhOYUFzN1Q5bkF1SCIsInN1YiI6IjE1MzgyNjAyODI1Iiwic2J0IjoibmlrZTpwbHVzIn0.NWBoumQUOrauh7heHkPmHrx4XKM65uhy-AI5zhW-pu-CkBtfsR0qY0G50EG9qFeut2fdpL39hAT8i7r1zd-0z93r8KTEQ9nn14rfp1WjofJxqYAj5B23-ArO_shR09450l4XEpYrfUtV8gDykzSo7JRS3yjXGcT2jRBGAhwmfIXwhsOqo5Eti2mSz7lz790rkTfPyAckIkFSQ91eYbt3r_3EQj-Heql2poDbaEotGBcG-KDCT7nvnIMi34eff5IW-WPXYZ0Hnccjt19tYzg9Y79aTMQzZK14KVNRKFGrEC58xFYBXKZQDStdVJ7RSt39JQZUvsI4W0nCWLyaPfixxg",
#         'cache-control': "no-cache",
#         'User-Agent': "SNKRS/3.4.1 (iPhone; iOS 10.3; Scale/3.00)",
#         'X-NewRelic-ID': "VQYGVF5SCBADUVBRBgAGVg==",
#         'Cookie': 'AnalysisUserId=ea247d5a-e446-406a-9c71-974b98338365; NIKE_COMMERCE_COUNTRY=CN; NIKE_COMMERCE_LANG_LOCALE=zh_CN; siteCatalyst_sample=32; dreamcatcher_sample=38; neo_sample=18; guidU=da01129f-3e2b-4bf4-c3ff-6705a1a09a71; neo.swimlane=77; slCheck=k2q2KLPtb38EmQvy8Ynb+408wa9qFHCrtYZk4s4EFmHEdVO+ohEboDznWkvbsU0TDVUwsqDtY4wj6niBCYzHjQ==; lls=3; llCheck=O6L24ZXTSPDUAosDCvU9FkL1I8gjMC0tHhXX2da8Euv6K03TwvtjUi2RmSg9wxoLSwyyvSq/QVHy0aY57xro/cqkM9HVOAQiWSZnBQKSTbzS1u/1aHUpEh/IPQb1LG8+85/FKM8oBqSK2BOKEKTZVg==; _abck=76775BDF3C8507EFE814F97DB686F9183CD21477442A00000B22615B04551E56~0~HSEowfaySoLCDI5WBKUUNppbi9d99cW1NDNFFw8svj0=~-1~-1; NIKE_COMMERCE_CCR=1533352781147; nike_cp=cnns_sz_071516_a_alnul_bz01; dreams_sample=39; cicPWIntercept=1; neo.experiments=%7B%22snkrs%22%3A%7B%7D%2C%22main%22%3A%7B%223333-interceptor-cn-jp%22%3A%22a%22%2C%223698-interceptor%22%3A%22a%22%7D%7D; _smt_uid=5b651b4f.2b4aa75f; _gscu_207448657=32931223yoxh1511; nike_locale=cn/zh_cn; _gscbrs_207448657=1; ajs_user_id=null; ajs_group_id=null; APID=EDB850C910C738FAC42B96657F1107BD.sin-344-app-ap-0; sls=1; CART_SUMMARY=%7B%22profileId%22+%3A%2217940739819%22%2C%22userType%22+%3A%22DEFAULT_USER%22%2C%22securityStatus%22+%3A%221%22%2C%22cartCount%22+%3A0%7D; exp.swoosh.user=%7B%22granted%22%3A0%7D; RES_TRACKINGID=924225756677951; ResonanceSegment=1; anonymousId=81243F6F1D29300A30E3C8E74D6A91B1; ajs_anonymous_id=%2281243F6F1D29300A30E3C8E74D6A91B1%22; CONSUMERCHOICE_SESSION=t; CONSUMERCHOICE=cn/zh_cn; bm_sz=1BB1B604808CC7065D2B19E82CA9A0AD~QAAQLNo4fffFvNVkAQAAh6sGI/Xzj1nqux9CuwuDuWorbCqYIeyDQ1kt/3NWrh9sngt15hT8IYuRasi5Y6odjKF//IUXgyTxKP1Bj88iazRIWTWQtTyk5bu0m8q5QZb7QNpbFyHFWw7B3Gh45Kr50aTlHlQa93gMc3JwqZbIGCqdBooMuY9Ddonc9w==; utag_main=_st:1533892932976$ses_id:1533892014193%3Bexp-session; guidS=9a1777c0-b465-46a2-972a-e784bdd6a45f; s_sess=%20tp%3D1068%3B%20s_ppv%3Dnikecom%25253Esize%252520and%252520fit%252520guide%25253EUnisex%252520Socks%252C96%252C96%252C1020%3B%20prevList2%3D%3B%20c51%3Dhorizontal%3B%20s_cc%3Dtrue%3B; guidSTimestamp=1533891134138|1533891141955; s_cc=true; AMCV_F0935E09512D2C270A490D4D%40AdobeOrg=793872103%7CMCIDTS%7C17753%7CMCMID%7C69232821038140284933362525925877410365%7CMCAAMLH-1534495942%7C11%7CMCAAMB-1534495942%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCAID%7CNONE%7CMCOPTOUT-1533891081.927%7CNONE%7CMCSYNCSOP%7C411-17760%7CvVersion%7C2.4.0; RT=\"sl=5&ss=1533891130972&tt=7079&obo=0&sh=1533891150794%3D5%3A0%3A7079%2C1533891145141%3D4%3A0%3A7077%2C1533891143973%3D3%3A0%3A7077%2C1533891140629%3D2%3A0%3A5788%2C1533891135193%3D1%3A0%3A3943&dm=nike.com&si=e9ecb566-6a6d-47cc-9fd7-c8c50514d996&bcn=%2F%2F36fb61b0.akstat.io%2F&ld=1533891150794&nu=https%3A%2F%2Fwww.nike.com%2Fcn%2Flaunch%2F&cl=1533891149781&r=https%3A%2F%2Fwww.nike.com%2Fcn%2Flaunch%2F&ul=1533891152703&hd=1533891152732"',
#         'Accept-Language': "zh-Hans-CN;q=1, en-CN;q=0.9",
#         'Content-Type': "application/json",
#         'authority': "api.nike.com",
#     }