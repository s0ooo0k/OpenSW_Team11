# Generated by Django 3.1.3 on 2020-12-16 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0007_remove_information_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='review_image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
