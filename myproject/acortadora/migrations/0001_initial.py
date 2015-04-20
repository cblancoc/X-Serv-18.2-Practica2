# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('real_url', models.CharField(max_length=64)),
                ('url_num', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
