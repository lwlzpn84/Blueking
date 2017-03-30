# -*- coding: utf-8 -*-
import json
import requests

requests.packages.urllib3.disable_warnings()
class SaltApi(object):
    """docstring for SaltApi"""
    def __init__(self):
        self.__user = "saltapi"
        self.__password = "L3OqVjVWuuWVjVq03L"
        self.__salt_url = "https://121.43.232.249:51341"
        self.__token_id = self.get_saltapi_token()
       

    def get_saltapi_token(self):
        '''
        @note: 登录获取saltapi token
        '''
        parmes={'eauth': 'pam' ,'username':self.__user,'password':self.__password}
        self.__salt_url += '/login'
        self.__my_headers = {
            'Accept': 'application/json'
        }       
        req = requests.post(self.__salt_url, headers=self.__my_headers,data=parmes, verify=False,timeout=2)
  
        content = json.loads(req.content)
        token = content["return"][0]['token']
        return token   

    # run salt cmd
    def saltCmd(self, params):
        '''执行salt操作'''
        my_headers = {
            'Accept': 'application/json',
            'X-Auth-Token':  self.__token_id
        }
        self.__salt_url = self.__salt_url.strip('/login')
        try:
            req = requests.post(self.__salt_url,data=params,headers=my_headers,verify=False)
            return req.content
        except IOError:
            raise IOError  

    def get_allhostname(self, params):
        '''执行salt操作'''
        my_headers = {
            'Accept': 'application/json',
            'X-Auth-Token':  self.__token_id
        }
        self.__salt_url = self.__salt_url.strip('/login')
        try:
            req = requests.post(self.__salt_url,data=params,headers=my_headers,verify=False)
            return req.content
        except IOError:
            raise IOError  
 

    def get_minions(self, host):
    	'''
    	@note: 收集主机minion信息
    	'''
        my_headers = {
            'Accept': 'application/json',
            'X-Auth-Token': self.__token_id
        }
        url = self.__salt_url.strip('/login') + ('/minions/%s' % host)
        
        req = requests.get(url, headers=my_headers, verify=False)
        json_data = json.loads(req.content)
        

        hostname = host.encode('raw_unicode_escape')
        release = json_data['return'][0]["%s" % host]["osfullname"].encode('raw_unicode_escape') + ' ' + json_data['return'][0]["%s" % host]["osrelease"].encode('raw_unicode_escape')
        kernelrelease = json_data['return'][0]["%s" % host]["kernelrelease"].encode('raw_unicode_escape')
        num_cpus = json_data['return'][0]["%s" % host]["num_cpus"]
        cpu_type= json_data['return'][0]["%s" % host]["cpu_model"].encode('raw_unicode_escape')
        mem_total = json_data['return'][0]["%s" % host]["mem_total"]
        private_ip = json_data['return'][0]["%s" % host]["ip4_interfaces"]["eth0"][0].encode('raw_unicode_escape')
        info = {
            'hostname': hostname,
            'os_release': release,
            'mem_total': mem_total,
            'num_cpus': num_cpus,
            'cpu_type':cpu_type,
            'private_ip': private_ip,
            'public_ip': '',
            'kernelrelease': kernelrelease
        }
        return info          

