# Generated by Django 3.1.7 on 2021-03-22 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0010_auto_20210321_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restarantinfo',
            name='rest_image',
            field=models.ImageField(blank=True, default='foodproject\x0coods\\placehold_stock.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='restarantinfo',
            name='rest_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
