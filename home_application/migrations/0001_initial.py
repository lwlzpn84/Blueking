# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u540d')),
                ('public_ip', models.CharField(max_length=30, verbose_name='\u516c\u7f51IP')),
                ('private_ip', models.CharField(max_length=30, verbose_name='\u5185\u7f51IP')),
                ('mem_total', models.CharField(max_length=30, verbose_name='\u603b\u5185\u5b58')),
                ('cpu_type', models.CharField(max_length=120, verbose_name='CPU\u7c7b\u578b')),
                ('num_cpus', models.CharField(max_length=30, verbose_name='CPU\u9897\u6570')),
                ('os_release', models.CharField(max_length=30, verbose_name='\u7cfb\u7edf\u7248\u672c')),
                ('kernelrelease', models.CharField(max_length=120, verbose_name='\u5185\u6838\u7248\u672c')),
            ],
        ),
    ]
