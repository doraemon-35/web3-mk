# Generated by Django 3.2.19 on 2023-08-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_list', '0003_all_pro_list_pro_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_pro_list',
            name='pro_type',
            field=models.CharField(choices=[('gt', 'GENERAL')], default=(('gt', 'GENERAL'),), max_length=50, null=True),
        ),
    ]
