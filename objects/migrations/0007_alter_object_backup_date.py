# Generated by Django 4.2.11 on 2024-04-28 09:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0006_alter_object_backup_date_alter_object_object_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='backup_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]