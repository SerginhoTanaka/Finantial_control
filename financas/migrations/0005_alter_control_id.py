# Generated by Django 4.2.3 on 2023-08-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0004_control_account_control_category_control_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
