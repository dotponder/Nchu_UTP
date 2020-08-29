# Generated by Django 3.0.5 on 2020-08-29 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20200830_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pay_method',
            field=models.SmallIntegerField(choices=[(2, '微信支付'), (1, '当面付款'), (3, '支付宝')], default=1, verbose_name='支付方式'),
        ),
    ]