# Generated by Django 1.11.5 on 2017-11-24 14:47
from __future__ import unicode_literals

from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("product", "0036_auto_20171115_0608")]

    operations = [TrigramExtension()]
