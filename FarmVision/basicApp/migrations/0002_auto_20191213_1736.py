# Generated by Django 3.0 on 2019-12-13 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crop',
            old_name='waterRequirementInMM',
            new_name='maxwaterRequirementInMM',
        ),
        migrations.AddField(
            model_name='crop',
            name='minwaterRequirementInMM',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
