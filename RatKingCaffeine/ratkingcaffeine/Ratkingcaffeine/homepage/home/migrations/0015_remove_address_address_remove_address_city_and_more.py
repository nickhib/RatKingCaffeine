# Generated by Django 4.1.4 on 2022-12-13 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_userinformation_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='address',
        ),
        migrations.RemoveField(
            model_name='address',
            name='city',
        ),
        migrations.RemoveField(
            model_name='address',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='userinformation',
            name='address',
            field=models.CharField(default=1, max_length=280),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinformation',
            name='city',
            field=models.CharField(default=1, max_length=280),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinformation',
            name='zipcode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
