# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-07 18:37
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import ipam.fields

class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0021_vrf_ordering'),
    ]

    operations = [
        migrations.CreateModel(
            name='WLANGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='wlan_groups', to='dcim.Site')),
            ],
            options={
                'ordering': ['site', 'name'],
                'verbose_name': 'WLAN group',
                'verbose_name_plural': 'WLAN groups',
            },
        ),
 
        migrations.AlterUniqueTogether(
            name='wlangroup',
            unique_together=set([('site', 'name'), ('site', 'slug')]),
        ),

        migrations.CreateModel(
            name='WLAN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('ssid', models.CharField(max_length=64, verbose_name='SSID')),
                ('name', models.CharField(max_length=64)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Active'), (2, 'Planned'), (3, 'Reserved'), (4, 'Deprecated')], default=1, verbose_name='Status')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wlans', to='ipam.Role')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='wlans', to='dcim.Site')),
                ('group',models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='wlans', to='ipam.WLANGroup')),
                ('description',models.CharField(blank=True, max_length=100)),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='wlans', to='tenancy.Tenant')),
            ],
            options={
                'ordering': ['site', 'group', 'ssid'],
                'verbose_name': 'WLAN',
                'verbose_name_plural': 'WLANs',
            },
        ),
        migrations.AlterUniqueTogether(
            name='wlan',
            unique_together=set([('group', 'name'), ('group', 'ssid')]),
        ),
    ]
