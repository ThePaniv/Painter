# Generated by Django 2.0.2 on 2018-02-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('Video', models.FileField(upload_to='Video')),
                ('Description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]