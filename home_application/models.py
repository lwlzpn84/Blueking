# -*- coding: utf-8 -*-

from django.db import models




class Hostinfo(models.Model):

    hostname = models.CharField(u"主机名",max_length=30)
    public_ip = models.CharField(u"公网IP",max_length=30)
    private_ip = models.CharField(u"内网IP",max_length=30)
    mem_total = models.CharField(u"总内存",max_length=30)
    cpu_type = models.CharField(u"CPU类型",max_length=120)
    num_cpus = models.CharField(u"CPU颗数",max_length=30)
    os_release = models.CharField(u"系统版本",max_length=30)
    kernelrelease = models.CharField(u"内核版本",max_length=120)

    def to_json(self):
        return {
        		'id':self.id,
                'hostname' : self.hostname,
                'public_ip' : self.public_ip,
                'private_ip' : self.private_ip,
                'mem_total' : self.mem_total,
                'cpu_type'  : self.cpu_type,
                'num_cpus' : self.num_cpus,
                'os_release': self.os_release,
                'kernelrelease': self.kernelrelease
        }
