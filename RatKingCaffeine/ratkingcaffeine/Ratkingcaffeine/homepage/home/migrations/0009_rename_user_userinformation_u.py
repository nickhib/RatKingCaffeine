# Generated by Django 4.1.1 on 2022-11-27 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_address_products_userinformation_delete_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinformation',
            old_name='user',
            new_name='u',
        ),
    ]
