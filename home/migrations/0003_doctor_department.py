# Generated by Django 4.0.6 on 2023-07-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
