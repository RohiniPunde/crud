# Generated by Django 3.0.3 on 2020-08-19 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0008_auto_20200819_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
