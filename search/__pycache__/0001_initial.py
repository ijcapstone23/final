# Generated by Django 4.2.4 on 2023-09-06 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductLst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=248)),
                ('shop_name', models.CharField(max_length=59)),
                ('price', models.IntegerField(default=0)),
                ('detail', models.CharField(max_length=59248)),
                ('url', models.CharField(max_length=248)),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.productlst')),
            ],
        ),
    ]