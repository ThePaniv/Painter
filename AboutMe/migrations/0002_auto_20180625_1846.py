# Generated by Django 2.0.4 on 2018-06-25 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutMe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='EngText',
            field=models.TextField(blank=True, null=True),
        ),
    ]