# Generated by Django 4.1.4 on 2022-12-13 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_userinformation_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinformation',
            old_name='address1',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='userinformation',
            old_name='city1',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='userinformation',
            old_name='zipcode1',
            new_name='zipcode',
        ),
    ]