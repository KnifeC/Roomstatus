# Generated by Django 2.1.2 on 2019-02-25 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Netstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.TextField()),
                ('updatetime', models.DateTimeField()),
            ],
        ),
    ]