# Generated by Django 4.1.4 on 2022-12-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, default='users/users_main_photos/default.jpg', upload_to='users/users_main_photos/'),
        ),
    ]
