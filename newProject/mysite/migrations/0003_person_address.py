# Generated by Django 3.2.6 on 2021-08-22 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20210821_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mysite.address'),
            preserve_default=False,
        ),
    ]
