# Generated by Django 3.2 on 2021-05-02 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.IntegerField()),
                ('brand', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('ram', models.IntegerField()),
                ('storage', models.IntegerField()),
                ('price', models.IntegerField()),
                ('stock_qty', models.IntegerField()),
                ('availibility', models.CharField(choices=[('AVAILABLE ', 'Item Ready to be Sold'), ('SOLD', 'Item Soldout'), ('RESTOCKING', 'Item will be Restocked in a few Days')], default='AVAILABLE', max_length=50)),
            ],
        ),
    ]
