# Generated by Django 3.0.3 on 2020-08-14 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0004_auto_20200814_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
