# Generated by Django 5.1.6 on 2025-02-09 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_contacted', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(default='', max_length=750)),
                ('message', models.TextField()),
            ],
        ),
    ]
