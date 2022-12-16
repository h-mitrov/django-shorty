# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_field', models.URLField(max_length=500)),
                ('personal', models.BooleanField(default=False)),
                ('personal_slug', models.CharField(max_length=125, null=True, blank=True)),
                ('status', models.CharField(max_length=10)),
                ('private', models.BooleanField(default=False)),
                ('private_password', models.CharField(max_length=25, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, ondelete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
