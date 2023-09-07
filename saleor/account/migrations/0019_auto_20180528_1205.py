# Generated by Django 2.0.3 on 2018-05-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("account", "0018_auto_20180426_0641")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="addresses",
            field=models.ManyToManyField(
                blank=True, related_name="user_addresses", to="account.Address"
            ),
        )
    ]
