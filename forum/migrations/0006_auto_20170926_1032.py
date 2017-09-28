# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20170925_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='parent_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='avatar_id',
            field=models.IntegerField(),
        ),
    ]