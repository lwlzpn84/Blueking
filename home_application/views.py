# -*- coding: utf-8 -*-
from common.mymako import render_mako_context
from saltapi.saltapi import SaltApi
from models import Hostinfo
import json
def index(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/opsplatform/index.html')



def server_list(request):
    """
    @note: 服务器列表
    """
    # # 获取所有server的hostname
    # client = SaltApi()
    # params = {'client': 'local', 'fun': 'test.ping', 'tgt': '*'}
    # json_data = client.get_allhostname(params)
    # data = dict(json.loads(json_data)['return'][0])
    # hostname_list = []
    # [ hostname_list.append(i) for i in data.keys() ]
    


    # # 获取所有server的hostname
    # for host in hostname_list:

    #     all_host_info = dict(client.get_minions(host).items())
    
    #     try:
    #         host_record = Hostinfo(
    #                     hostname=all_host_info['hostname'],
    #                     private_ip=all_host_info['private_ip'],
    #                     public_ip=all_host_info['public_ip'],
    #                     mem_total=all_host_info['mem_total'],
    #                     cpu_type=all_host_info['cpu_type'],
    #                     num_cpus=all_host_info['num_cpus'],
    #                     os_release=all_host_info['os_release'],
    #                     kernelrelease=all_host_info['kernelrelease']
    #                     )
    #         host_record.save()
    #         print u'导入主机 %s 成功！' % all_host_info['hostname']
    #     except Exception,e:
    #         print e

    # # 从数据库中读取
    host_list = Hostinfo.objects.all()   
    data = []
    [ data.append(i.to_json()) for i in host_list ]
    title = ["#",u'主机名',u'内网IP',u'外网IP',u"总内存",u"CPU类型",u"CPU颗数",u"系统版本",u"内核版本",u"操作"]
     
    return render_mako_context(request, '/home_application/opsplatform/server_list.html',{'title':title,"data":data})

