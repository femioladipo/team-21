# Generated by Django 2.1.2 on 2018-11-10 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0010_auto_20181110_0708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersurvey',
            old_name='question',
            new_name='survey_question',
        ),
    ]