# Generated by Django 4.2.8 on 2023-12-23 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_created_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['title']},
        ),
    ]
