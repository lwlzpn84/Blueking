# -*- coding: utf-8 -*-
from common.mymako import render_mako_context, render_json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from common.log import logger
from saltapi.saltapi import SaltApi
from django.http import HttpResponse
from models import Hostinfo
import json
def index(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/opsplatform/index.html')

def get_server_info(request):
    '''
    @note: 通过saltapi获取所有minion主机的服务器信息，填入写入数据库中
    '''
    # 获取所有server的hostname
    if request.method == "POST":
        client = SaltApi()
        params = {'client': 'local', 'fun': 'test.ping', 'tgt': '*'}
        json_data = client.get_allhostname(params)
        data = dict(json.loads(json_data)['return'][0])
        hostname_list = []
        [ hostname_list.append(i) for i in data.keys() ]
        
        # 获取所有server的hostname
        for host in hostname_list:

            all_host_info = dict(client.get_minions(host).items())
        
            try:
                host_record = Hostinfo(
                            hostname=all_host_info['hostname'],
                            private_ip=all_host_info['private_ip'],
                            public_ip=all_host_info['public_ip'],
                            mem_total=all_host_info['mem_total'],
                            cpu_type=all_host_info['cpu_type'],
                            num_cpus=all_host_info['num_cpus'],
                            os_release=all_host_info['os_release'],
                            kernelrelease=all_host_info['kernelrelease']
                            )
                host_record.save()
                print u'导入主机 %s 成功！' % all_host_info['hostname']
            except Exception,e:
                print e

def server_list(request):
    """
    @note: 服务器列表
    """


    # # 从数据库中读取
    host_list = Hostinfo.objects.all()   
    data = []
    [ data.append(i.to_json()) for i in host_list ]
    title = ["#",u'主机名',u'内网IP',u'外网IP',u"总内存",u"CPU类型",u"CPU颗数",u"系统版本",u"内核版本",u"操作"]
     
    return render_mako_context(request, '/home_application/opsplatform/server_list.html',{'title':title,"data":data})

@csrf_exempt
def delete_server(request):
    '''
    @note: 从数据库中删除已经存在的主机
    '''
    delete_host = request.GET.get('host')
    
    try:
        Hostinfo.objects.filter(hostname=delete_host).delete()
        result = {'result': True, 'message': u"删除主机 %s 成功." % delete_host}
        
    except Exception, e:
        logger.error(u"删除纪录失败，%s" % e)
        result = {'result': False, 'message': u"删除纪录失败，%s" % e}
    return render_json(result)
