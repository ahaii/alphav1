# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-03 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, verbose_name='名字')),
                ('Email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('Head_img', models.ImageField(default='static/alpha/uploads/UserHeadImg/default.jpg', height_field=160, upload_to='static/alpha/uploads/UserHeadImg', verbose_name='用户头像', width_field=160)),
                ('Role', models.SmallIntegerField(choices=[(0, 'user'), (1, 'admin')], default=0)),
            ],
        ),
    ]
