# Generated by Django 4.0.4 on 2022-06-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_alter_useraccount_image_alter_useraccount_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
    ]
