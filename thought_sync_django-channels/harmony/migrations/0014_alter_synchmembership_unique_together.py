# Generated by Django 4.2.13 on 2024-07-06 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("harmony", "0013_alter_note_id"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="synchmembership", unique_together={("synch", "member")},
        ),
    ]
