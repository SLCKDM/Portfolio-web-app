# Generated by Django 3.0.4 on 2021-06-16 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='description',
            field=models.TextField(max_length=1250),
        ),
    ]
