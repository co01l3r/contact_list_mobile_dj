# Generated by Django 4.1.3 on 2022-12-02 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_alter_contact_web'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='web',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
