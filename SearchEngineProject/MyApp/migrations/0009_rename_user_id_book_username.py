# Generated by Django 5.0.3 on 2024-05-15 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0008_rename_user_id_question_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='user_id',
            new_name='username',
        ),
    ]