# Generated by Django 5.0.4 on 2024-04-28 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BorderPay', '0002_remove_employee_id_remove_employee_userid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='denomination',
        ),
    ]