# Generated by Django 2.1 on 2018-08-02 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180802_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='armor_class',
            field=models.IntegerField(default=12),
        ),
        migrations.AlterField(
            model_name='monster',
            name='hit_points',
            field=models.IntegerField(null=True),
        ),
    ]
