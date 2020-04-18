
# coding: utf-8

# In[ ]:


#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
import urllib
import os,sys
import re
from urllib.request import urlopen, URLError


class Ximalaya_file():
    _randomSeed = 0
    _cgStr = ""

    def __init__(self, seed):
        self._randomSeed = seed
        self.cg_hun()

    def cg_hun(self):
        str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/\\:._-1234567890"
        str_len = len(str)
        count = 0
        while count < str_len:
            index = int(self.ran() * len(str))
            self._cgStr += str[index]
            str = "".join(str.split(str[index]))
            count += 1

    def cg_fun(self, str):
        str = str.split("*")
        temp_str = ""
        str_len = len(str) - 1
        count = 0
        while count < str_len:
            temp_str += self._cgStr[int(str[count])]
            count += 1
        return temp_str

    def ran(self):
        self._randomSeed = (211 * self._randomSeed + 30031) % 65536
        return float(self._randomSeed) / 65536

    def cg_decode(self, str):
        temp_str = ""
        str_len = len(str)
        count = 0
        while count < str_len:
            temp = str[count]
            temp_index = self._cgStr.indexOf(temp)
            if -1 != temp_index:
                temp += temp_index + "*"
            count += 1
        return temp_str


def from_char_code(a, *b):
    return chr(a % 65536) + ''.join([chr(i % 65536) for i in b])


def get_encrypted_file_name(seed, file_id):
    file_name = Ximalaya_file(seed).cg_fun(file_id)
    return file_name if "/" == file_name[0] else "/" + file_name


def aaa(e, t):
    t = t
    n = ""
    r = []
    a = 0
    i = ""
    o = 0
    while 256 > o:
        r.append(o)
        o += 1
    o = 0
    while 256 > o:
        a = (a + r[o] + ord(e[o % len(e)])) % 256
        n = r[o]
        r[o] = r[a]
        r[a] = n
        o += 1

    u = a = o = 0
    while u < len(t):
        o = (o + 1) % 256
        a = (a + r[o]) % 256
        n = r[o]
        r[o] = r[a]
        r[a] = n
        i += from_char_code(ord(t[u]) ^ r[(r[o] + r[a]) % 256])
        u += 1
    return i


def get_encrypted_file_params(ep):
    o = aaa("xm", u"Ä[ÜJ=Û3Áf÷N")
    u = [19, 1, 4, 7, 30, 14, 28, 8, 24, 17, 6, 35, 34, 16, 9, 10, 13, 22, 32, 29, 31, 21, 18, 3, 2, 23, 25, 27, 11, 20,
         5, 15, 12, 0, 33, 26]
    e = "d" + o + "9"
    tt = u
    n = []
    r = 0
    while r < len(e):
        a = ord(e[r]) - 97 if "a" <= e[r] and "z" >= e[r] else ord(e[r]) - 48 + 26
        i = 0
        while 36 > i:
            if tt[i] == a:
                a = i
                break
            i += 1
        n.append(from_char_code(a - 26 + 48) if 25 < a else from_char_code(a + 97))
        r += 1
    var1 = "".join(n)
    var2 = bbb(ep)

    t = (aaa(var1, var2)).split("-")

    return {
        "sign": t[1] if len(t) >= 2 else "",
        "buy_key": t[0] if len(t) >= 1 else "",
        "token": t[2] if len(t) >= 3 else "", 
        "timestamp": t[3] if len(t) >= 4 else ""
    }


def bbb(e):
    if len(e) <= 0:
        return ""
    o = [- 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63,
         52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8,
         9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26,
         27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
         51, -1, -1, -1, -1, -1]
    a = len(e)
    r = 0
    i = ""
    while r < a:
        while True:
            t = o[255 & ord(e[r])]
            r += 1
            if not (r < a and -1 == t):
                break
        if -1 == t:
            break

        while True:
            n = o[255 & ord(e[r])]
            r += 1
            if not (r < a and -1 == n):
                break
        if -1 == t:
            break
        i += from_char_code(t << 2 | (48 & n) >> 4)

        while True:
            t = 255 & ord(e[r])
            if 61 == t:
                return i
            t = o[t]
            r += 1
            if not (r < a and -1 == t):
                break
        if -1 == t:
            break
        i += from_char_code((15 & n) << 4 | (60 & t) >> 2)

        while True:
            n = 255 & ord(e[r])
            if 61 == n:
                return i
            n = o[n]
            r += 1
            if not (r < a and -1 == n):
                break
        if -1 == n:
            break
        i += from_char_code((3 & t) << 6 | n)
    return i


def url_param(dict):
    first_flag = True
    params = ""
    for key, values in dict.items():
        if first_flag:
            first_flag = False
        else:
            params += "&"
        params += key + "=" + values


def get(url, *params):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'connection': 'keep-alive', 
    }
    
    param = params[0] if len(params) else {}
    resp = requests.get(url, headers=headers,cookies=CUSTOM_COOKIE, params=param)
    return resp


def get_time():
    request = get("https://www.ximalaya.com/revision/time")
    if request.status_code == 200:
        return request.text
    else:
        print ("Requesting server time failed")


def get_tdk(url):
    resp = get("https://www.ximalaya.com/revision/seo/getTdk", {"typeName": "ALBUM", "uri": url})
    # resp = get("https://www.ximalaya.com/revision/seo/getTdk?typeName=ALBUM&uri=%2Fyoushengshu%2F19421464%2F")
    if resp.status_code == 200:
        resp_data = json.loads(resp.text)
        data = resp_data["data"]
        if resp_data["ret"] == 200:
            print (data["tdkMeta"]["title"])
    else:
        print ("get_tdk() request error")
        return False
    return True


def get_tracks(album_id, page_info):
    #https://www.ximalaya.com/revision/play/album?albumId=11774913&pageNum=1
    tracks_resp = get('https://www.ximalaya.com/revision/album/v1/getTracksList',
                      {'albumId': album_id, 'pageNum': page_info["pageNum"]})
    tracks = []
    if tracks_resp.status_code == 200:
        resp_data = json.loads(tracks_resp.text)
        data = resp_data["data"]
        if resp_data["ret"] == 200:
            page_info["totalCount"] = data["trackTotalCount"]
            # 打印下载信息
            print ( u"[total track number]:%s" % (page_info["totalCount"]))
            print (u"[current page]: %s" % (page_info["pageNum"]))
            tracks = data["tracks"]
        else:
            print (resp_data["msg"])
    else:
        print ("get_tracks() request error")

    return tracks

def get_file_download_url_free(track_id):
     
    file_data = get("http://mobile.ximalaya.com/v1/track/baseInfo?device=iPhone&trackId="+str(track_id))
     
    file_download_url = ""
    if file_data.status_code == 200:
        resp_data = json.loads(file_data.text)
        if resp_data['ret'] != 0:
            print ("Error occured while download tracks#",track_id )
            print ("Error message:"+ resp_data['msg'])
            sys.exit(resp_data['ret'])
     
         
        #sys.exit()
        # 打印下载信息
        
        print (u"[Downloading]:%s" % (resp_data["title"]))
        file_download_url = resp_data["playUrl64"]
    else:
        print ("get_file_download_url() request error")
    return file_download_url

def get_file_download_url(track_id):
    time = get_time()
    file_data = get("https://mpay.ximalaya.com/mobile/track/pay/" + str(track_id),
                    {"device": "pc", "isBackend": "false", "_": time})
    
    file_download_url = ""
    if file_data.status_code == 200:
        resp_data = json.loads(file_data.text)
        if resp_data['ret'] != 0:
            print ("Error occured while downloading track#",track_id )
            print ("Error message:"+ resp_data['msg'])
            sys.exit(resp_data['ret'])
            
            
        # 打印下载信息
        print (u"[Downloading]:%s" % (resp_data["title"]))
        print (u"[File size]: %s KB" % (resp_data["totalLength"] / 1024))
        file_name = get_encrypted_file_name(resp_data["seed"], resp_data["fileId"])
        file_params = get_encrypted_file_params(resp_data["ep"])
        file_params["duration"] = resp_data["duration"]
        file_download_url = resp_data["domain"] + "/download/" + resp_data[
            "apiVersion"] + file_name + "?" + urllib.parse.urlencode(file_params)
    else:
        print ("get_file_download_url() request error")
    return file_download_url


def download_file(file_name, file_download_url, download_path):
    if os.path.exists(download_path + "/" + file_name) and os.path.isfile(download_path + "/" + file_name):
        print (u"%s exists，skipping" % (file_name))
        return
    resp_data = get(file_download_url)
    
    chunk_size = 1024
    size = 0
    content_size = float(resp_data.headers['content-length'])
    if resp_data.status_code == 200:
        with open(download_path + "/" + file_name, "wb") as file:
            for data in resp_data.iter_content(chunk_size=chunk_size):
                file.write(data)
                size += len(data)
                # print '\r' + u'[%s下载进度]:%s%.2f%%' % (
                # file_name, '>' * int(size * 50 / content_size), size / float(content_size) * 100)
    else:
        print ("Download failed!")
        
def download():
    global CUSTOM_COOKIE 
     
    download_url = input("Enter album link: ")
    #download_url = "https://www.ximalaya.com/youshengshu/14356532"
    download_path = input("Destination folder: ")
    if len(download_path) <=0:
        download_path="./tmp"
    
    if paid == "2":
        #TOKEN = input("Please enter cookie: ")
        TOKEN = os.getenv('cookie')

        CUSTOM_COOKIE = {
             "1&_token":TOKEN,
            }

    else: CUSTOM_COOKIE = {}

    
    if len(download_url) <= 0:
        print ("Resolve link error")
        return
    if len(download_path) <= 0:
        print ("Please enter destination folder")
        return
    if not os.path.exists(download_path):
        os.mkdir(download_path)

    download_url = download_url.replace("http://", "").replace("https://", "")
    params = download_url.split("/")
    if len(params) < 3:
        print ("Error when resolving link")
        return

    page_info = {
        "totalCount": -1,
        "pageNum": 1,
        "pageSize": 0
    }

    start_page_size = input("Please enter start page number(blank default first page):")
    if len(start_page_size) > 0 and start_page_size.isdigit():
        try:
            page_info["pageNum"] = int(start_page_size)
        except ValueError:
            print ("Incorrect page number")
            return

    uri = "/" + params[1] + "/" + params[2] + "/"
    album_id = params[2]

    if len(album_id) > 0:
        # 下载信息
        if not get_tdk(uri):
            return
        # 获取文件列表
        while True:
            tracks = get_tracks(album_id, page_info)
            if len(tracks) > 0:
                for track in tracks:
                    if paid == "2":
                        file_download_url = get_file_download_url(track["trackId"])
                        download_file(track["title"] + ".m4a", file_download_url, download_path)
                        print ("=" * 100)
                    else:
                        file_download_url=get_file_download_url_free(track["trackId"])
                        download_file(track["title"] + ".mp3", file_download_url, download_path)
                        print ("=" * 100)
                  
                    # print file_download_url
                    # 下载文件
                    
            else:
                break
            page_info["pageNum"] += 1
            if not (page_info["pageSize"] < page_info["pageNum"]):
                break

    print ("Download Finished！")


def main():
    global paid
    paid = input ("Is this free audio?(1: Yes| 2: No) ")
    #       while True:
#       operation_order = input("Choose what to do: (1: Download 2: Exit): ")
        
    operation_order="1"
    if operation_order == "1":
        download()
    elif operation_order == "2":
        print ("Bye!")
            #break
    else:
        print ("Command entered incorrectly")


if __name__ == '__main__':
    main()


