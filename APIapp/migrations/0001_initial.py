# Generated by Django 4.2.1 on 2023-05-28 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='api',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('tecnologia', models.CharField(max_length=200)),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
