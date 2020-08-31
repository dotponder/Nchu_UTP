# Generated by Django 3.0.5 on 2020-08-30 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20200830_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.SmallIntegerField(choices=[(3, '待评价'), (1, '待付款'), (4, '已完成'), (2, '待交易')], default=2, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay_method',
            field=models.SmallIntegerField(choices=[(2, '微信支付'), (1, '当面付款'), (3, '支付宝')], default=1, verbose_name='支付方式'),
        ),
    ]
