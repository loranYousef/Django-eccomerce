# Generated by Django 4.2 on 2023-11-23 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_cartdetail_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_status',
            field=models.CharField(choices=[('Inprogress', 'Inprogress'), ('Completed', 'Completed')], default='Inprogress', max_length=10),
        ),
    ]