# Generated by Django 4.2.8 on 2023-12-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_contact_email_contact_message_alter_contact_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]