# Generated by Django 5.0.3 on 2024-07-06 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0009_alter_add_product_name_alter_home_add_down_heading_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x000001B00DF4BA60>', max_length=200),
        ),
    ]
