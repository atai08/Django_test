# Generated by Django 2.2 on 2020-05-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='description',
            field=models.TextField(),
        ),
    ]
