# Generated by Django 2.1.2 on 2018-11-10 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0011_auto_20181110_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersurvey',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
