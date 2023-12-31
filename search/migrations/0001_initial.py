# Generated by Django 4.2.4 on 2023-09-12 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=248)),
                ('shop_name', models.CharField(max_length=59)),
                ('price', models.IntegerField(default=0)),
                ('detail', models.CharField(default=None, max_length=59248, null=True)),
                ('url', models.CharField(max_length=2480)),
                ('imgurl', models.CharField(default=None, max_length=2480, null=True)),
                ('star', models.FloatField(default=3.0)),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.product')),
            ],
        ),
    ]
