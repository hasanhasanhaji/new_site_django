# Generated by Django 4.2.8 on 2024-01-06 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
