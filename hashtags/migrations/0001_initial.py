# Generated by Django 3.0.8 on 2020-07-03 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]