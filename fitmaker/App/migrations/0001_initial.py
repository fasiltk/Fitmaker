# Generated by Django 4.2.5 on 2023-12-25 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=244)),
                ('password', models.CharField(max_length=244)),
                ('name', models.CharField(max_length=244)),
                ('phonenumber', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]