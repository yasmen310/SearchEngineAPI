# Generated by Django 5.0.3 on 2024-05-15 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_rename_track_book_track_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='track',
            new_name='track_id',
        ),
    ]