# Generated by Django 4.1.3 on 2022-12-04 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_contact_birthday_dayofyear_internal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='birthday_dayofyear_internal',
        ),
        migrations.AlterField(
            model_name='contact',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
