# Generated by Django 4.0.5 on 2022-06-22 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreDatabse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_code', models.CharField(max_length=300)),
                ('bill_date', models.DateTimeField(blank=True, null=True)),
                ('bill_no', models.IntegerField(blank=True, null=True)),
                ('item_count', models.IntegerField(blank=True, null=True)),
                ('sale_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]