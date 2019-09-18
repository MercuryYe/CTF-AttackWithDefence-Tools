#-*- coding: utf-8 -*-
import urllib
import urllib2
import httplib

# GET请求方式
def Type_get(url,flag,token):
    url = url + "?flag=" + flag + "&token=" + token # URL拼接可根据实际情况修改
    req = urllib2.Request(url)
    try:
        res = urllib2.urlopen(req).code # 获取反馈HTTP状态码
        return res
    except:
        print "[-] Url Error"

# POST请求方式
def Type_post(url,flag,token):
    post_data = {'flag':flag,'token':token} # POST数据可根据实际情况修改
    post_data_urlencode = urllib.urlencode(post_data)
    req = urllib2.Request(url = url,data = post_data_urlencode)
    try:
        res = urllib2.urlopen(req).code # 获取反馈HTTP状态码
        return res
    except:
        print "[-] Url Error"

if __name__ == '__main__':
    url = raw_input("[*] Enter the url that submit to flag: ")
    flag = raw_input("[*] Enter the flag: ")
    token = raw_input("[*] Enter the token: ")
    requests_method = raw_input("[*] Choose the request method [1:GET 2:POST]: ")
    if requests_method == 1 or "GET":
        result = Type_get(url, flag, token)
        if result == 200:
            print '[+] Submit Successed'
        else:
            print '[-] Submit Failed'
    elif requests_method == 2 or "POST":
        result = Type_post(url, flag, token)
        if result == 200:
            print '[+] Submit Successed'
        else:
            print '[-] Submit Failed'
    else:
        print "[-] Please check your requests method again[1:GET 2:POST]"