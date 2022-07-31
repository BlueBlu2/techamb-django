# Generated by Django 3.2.14 on 2022-07-31 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('publish_date', models.DateField(null=True)),
                ('price', models.FloatField()),
                ('appropriate', models.CharField(choices=[('u-8', 'Under 8'), ('8to15', '8-15'), ('adults', 'Adults')], max_length=20, null=True)),
            ],
        ),
    ]