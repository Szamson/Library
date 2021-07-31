# Generated by Django 3.2.5 on 2021-07-31 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
                ('isbn', models.CharField(max_length=20)),
                ('number_of_pages', models.IntegerField()),
                ('cover', models.CharField(max_length=1000)),
                ('language', models.CharField(max_length=20)),
            ],
        ),
    ]
