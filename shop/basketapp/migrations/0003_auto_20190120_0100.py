# Generated by Django 2.1.3 on 2019-01-19 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0002_auto_20190116_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product'),
        ),
    ]
