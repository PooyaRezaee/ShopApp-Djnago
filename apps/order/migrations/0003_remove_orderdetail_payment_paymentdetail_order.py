# Generated by Django 4.1.3 on 2022-12-06 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_paymentdetail_order_orderdetail_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='payment',
        ),
        migrations.AddField(
            model_name='paymentdetail',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.orderdetail'),
            preserve_default=False,
        ),
    ]
