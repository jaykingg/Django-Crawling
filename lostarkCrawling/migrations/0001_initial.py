# Generated by Django 3.0.7 on 2020-06-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loaCrawling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_Date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('title', models.CharField(max_length=16)),
                ('cristal', models.IntegerField()),
            ],
        ),
    ]
