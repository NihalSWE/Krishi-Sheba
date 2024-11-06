# Generated by Django 4.0.4 on 2022-05-14 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductItem', '0005_rename_f_customer_order_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machinery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('rent_perday', models.IntegerField()),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='machineryimg')),
                ('is_Available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rent_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('product_id', models.IntegerField(null=True)),
                ('product_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True)),
                ('confirm', models.BooleanField(default=False)),
            ],
        ),
    ]