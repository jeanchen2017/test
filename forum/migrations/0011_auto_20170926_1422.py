# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_auto_20170926_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='parent_id',
        ),
        migrations.AddField(
            model_name='post',
            name='parent_id',
            field=models.ManyToManyField(related_name='_post_parent_id_+', to='forum.Post'),
        ),
    ]
