# Generated by Django 3.2.9 on 2021-12-07 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crypto_tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cost_per_share', models.DecimalField(decimal_places=2, max_digits=4)),
                ('date', models.DateField(auto_now=True)),
                ('asset', models.CharField(choices=[('BTC', 'BITCOIN'), ('L1', 'LAYER1'), ('L2', 'LAYER2'), ('G', 'GAMING')], default='BTC', max_length=4)),
                ('long_or_short', models.CharField(choices=[('L', 'LONG'), ('S', 'SHORT')], default='L', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='stock_tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cost_per_share', models.DecimalField(decimal_places=2, max_digits=4)),
                ('date', models.DateField(auto_now=True)),
                ('asset', models.CharField(choices=[('E', 'Equites'), ('B', 'Bonds'), ('F', 'Futures')], default='E', max_length=3)),
                ('long_or_short', models.CharField(choices=[('L', 'LONG'), ('S', 'SHORT')], default='L', max_length=2)),
            ],
        ),
    ]
