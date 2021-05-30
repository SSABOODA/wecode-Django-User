# Generated by Django 3.2.3 on 2021-05-30 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=300)),
                ('phone_number', models.CharField(max_length=20, null=True, unique=True)),
                ('nickname', models.CharField(max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]