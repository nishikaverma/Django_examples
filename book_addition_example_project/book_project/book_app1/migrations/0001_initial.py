# Generated by Django 2.2 on 2019-06-04 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('book_name', models.CharField(max_length=30)),
                ('book_price', models.FloatField()),
                ('subject', models.CharField(max_length=30)),
                ('publish_date', models.DateField(null=True)),
            ],
        ),
    ]
