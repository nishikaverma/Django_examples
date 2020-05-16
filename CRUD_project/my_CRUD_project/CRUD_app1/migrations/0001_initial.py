# Generated by Django 2.2 on 2019-06-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_id', models.IntegerField()),
                ('e_name', models.CharField(max_length=30)),
                ('e_mail', models.EmailField(max_length=254)),
                ('e_sal', models.FloatField()),
            ],
        ),
    ]
