# Generated by Django 4.2.1 on 2023-06-07 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medications_For_Use_Of',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('제품명A', models.CharField(max_length=50)),
                ('disease', models.CharField(max_length=100)),
                ('admin', models.CharField(max_length=50)),
                ('성분', models.CharField(max_length=50)),
            ],
        ),
    ]