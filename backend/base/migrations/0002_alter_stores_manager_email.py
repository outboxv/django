# Generated by Django 4.1.3 on 2022-11-12 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores',
            name='manager_email',
            field=models.EmailField(max_length=254),
        ),
    ]