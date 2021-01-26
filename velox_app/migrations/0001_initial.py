# Generated by Django 3.1.3 on 2021-01-26 07:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CareersOpportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opportunity', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=40)),
                ('isActive', models.BooleanField(default=True)),
                ('skills', models.TextField()),
                ('responsibilities', models.TextField()),
                ('salary', models.ImageField(blank=True, null=True, upload_to='')),
                ('createdOn', models.DateField(default=datetime.datetime(2021, 1, 26, 7, 54, 22, 671411, tzinfo=utc))),
            ],
        ),
    ]
