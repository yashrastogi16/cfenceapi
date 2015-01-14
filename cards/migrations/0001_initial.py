# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cards',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cardnumber', models.BigIntegerField(unique=True)),
                ('cardexpiry', models.TextField()),
                ('cvv', models.IntegerField()),
                ('status', models.CharField(max_length=10, choices=[(b'0', b'Red'), (b'1', b'Amber'), (b'2', b'Green')])),
                ('cardtype', models.CharField(max_length=100)),
                ('user', models.ForeignKey(to='login.user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
