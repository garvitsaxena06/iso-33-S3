# Generated by Django 3.0.3 on 2020-02-23 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200224_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('contactno', models.CharField(max_length=10)),
                ('feed', models.CharField(max_length=100)),
            ],
        ),
    ]
