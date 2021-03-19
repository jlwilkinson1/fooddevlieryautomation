# Generated by Django 3.1.7 on 2021-03-17 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_auto_20210317_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restarantinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_image', models.ImageField(blank=True, upload_to='')),
                ('is_closed', models.BooleanField(default=False)),
                ('deliveries', models.BooleanField(default=True)),
                ('pickup', models.BooleanField(default=True)),
                ('cuisines', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('zip_code', models.PositiveSmallIntegerField()),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.offer')),
            ],
        ),
    ]