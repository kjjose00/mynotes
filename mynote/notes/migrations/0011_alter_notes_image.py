# Generated by Django 4.0.4 on 2022-06-28 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_alter_notes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
    ]
