#! _*_ coding:utf8 _*_

from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets
import assets.models


class ServerDetailModuleForm(ModelForm):
    class Meta:
        model = assets.models.Servers
        # 使用模型中的所有字段
        fields = '__all__'

    applications = forms.IntegerField(
        label='应用',
        widget=forms.CheckboxSelectMultiple(
            # choices=(
            #     (0, 'Nginx'),
            #     (1, 'ActiveMQ'),
            #     (2, 'MySQL'),
            #     (3, 'ZK'),
            #     (4, 'Kafka'),
            #     (5, 'Elastic'),
            #     (6, 'Redis'),
            #     (7, 'Sentinel'),
            #     (8, 'Logstash'),
            #     (9, 'Kibana'),
            #     (10, 'PHP'),
            #     (11, 'Mongo'),
            #     (12, 'Dubbo'),
            #     (13, 'Zabbix'),
            #     (14, 'Jenkins'),
            #     (15, 'Tomcat'),
            #     (16, 'Confluence'),
            #     (17, 'Gitlab'),
            #     (18, 'FastDFS'),
            #     (19, 'Zentao'),
            #     (20, 'Nexus'),
            #     (21, 'Keepalived'),
            #     (22, 'Haproxy'),
            # )
        ),
        required=True
    )
