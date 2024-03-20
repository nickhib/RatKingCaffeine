# Generated by Django 4.1.4 on 2022-12-13 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_address_city_remove_address_zipcode_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinformation',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userinformation',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userinformation',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='userinformation',
            name='address1',
            field=models.CharField(default=1, max_length=280),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinformation',
            name='city1',
            field=models.CharField(default=1, max_length=280),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinformation',
            name='zipcode1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]