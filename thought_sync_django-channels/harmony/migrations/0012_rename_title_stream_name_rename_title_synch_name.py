# Generated by Django 4.2.13 on 2024-07-03 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("harmony", "0011_alter_synch_picture_alter_synchmembership_member"),
    ]

    operations = [
        migrations.RenameField(model_name="stream", old_name="title", new_name="name",),
        migrations.RenameField(model_name="synch", old_name="title", new_name="name",),
    ]
