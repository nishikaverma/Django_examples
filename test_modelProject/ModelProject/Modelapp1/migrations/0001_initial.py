# Generated by Django 2.2 on 2019-06-01 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grocry_Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vegies', models.CharField(max_length=30)),
                ('price_per_kg', models.FloatField()),
            ],
        ),
    ]
