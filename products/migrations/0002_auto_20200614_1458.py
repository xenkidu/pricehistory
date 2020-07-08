# Generated by Django 2.1.5 on 2020-06-14 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='homedepot_url',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_chart',
            field=models.TextField(blank=True),
        ),
    ]
