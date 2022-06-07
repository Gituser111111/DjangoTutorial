# Generated by Django 4.0.5 on 2022-06-07 15:57

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
                ('user_account', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=15)),
                ('user_password', models.CharField(max_length=20)),
                ('user_career', models.CharField(max_length=15)),
                ('user_age', models.IntegerField(default=20)),
                ('user_income', models.IntegerField(default=0)),
            ],
        ),
    ]
