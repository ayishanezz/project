# Generated by Django 5.0.2 on 2024-03-07 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_products_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(default='Added', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_status',
            field=models.CharField(choices=[('Order Placed', 'Order Placed'), ('Cancelled', 'Cancelled'), ('Shipped', 'Shipped'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered')], default='Order Placed', max_length=100),
        ),
    ]
