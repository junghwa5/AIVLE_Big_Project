# Generated by Django 4.0 on 2023-06-12 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinformation', '0008_accountinfo_birthdate_accountinfo_dt_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountinfo',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]