# Generated by Django 5.1 on 2024-09-10 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managementapp', '0003_alter_task_table_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task_table',
            name='new_task',
        ),
    ]
