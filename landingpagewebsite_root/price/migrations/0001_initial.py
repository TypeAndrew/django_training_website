# Generated by Django 4.2.9 on 2024-02-05 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_value', models.CharField(max_length=20, verbose_name='Ціна')),
                ('pc_description', models.CharField(max_length=200, verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Ціна',
                'verbose_name_plural': 'Ціни',
            },
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_title', models.CharField(max_length=200, verbose_name='Послуга')),
                ('pt_old_price', models.CharField(max_length=200, verbose_name='Стара цінав')),
                ('pt_price', models.CharField(max_length=200, verbose_name='Нова ціна')),
            ],
            options={
                'verbose_name': 'Послуга',
                'verbose_name_plural': 'Послуги',
            },
        ),
    ]
