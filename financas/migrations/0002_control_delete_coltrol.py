# Generated by Django 4.2.3 on 2023-07-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(choices=[('Inter', 'Inter'), ('Caixa', 'Caixa'), ('Clear', 'Clear')], max_length=10)),
                ('payment_method', models.CharField(choices=[('Crédito', 'Crédito'), ('Débito', 'Débito')], max_length=10)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Coltrol',
        ),
    ]
