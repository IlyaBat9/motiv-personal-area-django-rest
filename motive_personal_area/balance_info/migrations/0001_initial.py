# Generated by Django 2.2.4 on 2019-10-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(default=0)),
                ('minutes', models.IntegerField(null=True)),
                ('sms', models.IntegerField(null=True)),
                ('traffic', models.IntegerField(null=True)),
            ],
        ),
    ]
