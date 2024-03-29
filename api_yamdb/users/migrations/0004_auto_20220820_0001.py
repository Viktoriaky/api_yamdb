# Generated by Django 2.2.16 on 2022-08-19 21:01

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220815_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.TextField(max_length=150, unique=True, validators=[users.validators.UsernameRegexValidator], verbose_name='Имя пользователя'),
        ),
    ]
