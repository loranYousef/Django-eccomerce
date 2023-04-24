# Generated by Django 4.2 on 2023-04-24 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.generate_code


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0004_orderdetail_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_status', models.CharField(choices=[('Inprogress', 'Inprogress'), ('Complete', 'Complete')], default='Inprogress', max_length=10)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='order_code',
            field=models.CharField(default=utils.generate_code.generate_code, max_length=10),
        ),
        migrations.CreateModel(
            name='CartDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField(default=1)),
                ('total', models.FloatField(blank=True, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_detail', to='orders.cart')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_product', to='product.product')),
            ],
        ),
    ]
