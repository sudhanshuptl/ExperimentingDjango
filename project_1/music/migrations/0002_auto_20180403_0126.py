# Generated by Django 2.0.3 on 2018-04-02 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='songs',
            new_name='Song',
        ),
    ]