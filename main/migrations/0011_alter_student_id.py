# Generated by Django 4.0.6 on 2023-07-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_events_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(default=10000, primary_key=True, serialize=False),
        ),
    ]