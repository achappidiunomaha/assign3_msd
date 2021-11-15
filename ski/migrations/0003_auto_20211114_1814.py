# Generated by Django 3.2.9 on 2021-11-15 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ski', '0002_auto_20211114_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='state',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='zipcode',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]
