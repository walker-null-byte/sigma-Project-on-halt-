# Generated by Django 4.0.2 on 2022-02-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('passw', models.CharField(max_length=50)),
                ('confPassw', models.CharField(max_length=50)),
            ],
        ),
    ]
