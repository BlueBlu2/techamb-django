# Generated by Django 3.2.14 on 2022-07-31 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskII', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taskII.book'),
        ),
    ]
