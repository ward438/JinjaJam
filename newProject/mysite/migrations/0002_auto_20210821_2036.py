# Generated by Django 3.2.6 on 2021-08-22 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip', models.CharField(max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='address',
        ),
        migrations.DeleteModel(
            name='People',
        ),
    ]
