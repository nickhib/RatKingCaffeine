# Generated by Django 4.1.1 on 2022-11-26 23:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=280)),
                ('city', models.CharField(max_length=280)),
                ('zipcode', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField()),
                ('productname', models.CharField(max_length=280)),
                ('productcategory', models.CharField(max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='userinformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=280)),
                ('First_name', models.CharField(max_length=280)),
                ('Last_name', models.CharField(max_length=280)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='userprofile',
        ),
    ]