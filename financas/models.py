from django.db import models


class Control(models.Model):
    ACCOUNTS = [
        ('Inter', 'Inter'),
        ('Caixa', 'Caixa'),
        ('Clear', 'Clear')
    ]

    TYPES = [
        ('Receita','Receita'),
        ('Despesa','Despesa'),
        ('Investimento','Investimento')
    ]
    CATEGORIES = [
        ('Comida','Comida'),
        ('Carro','Carro'),
        ('Outros','Outros')
    ]
    account = models.CharField(max_length=10, choices=ACCOUNTS, null=True)
    type = models.CharField(max_length=30, choices=TYPES,null=True)
    date = models.DateField(null=True)
    category = models.CharField(max_length=30,choices=CATEGORIES,null=True)
    description = models.CharField(max_length=100,null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2,null=True)
