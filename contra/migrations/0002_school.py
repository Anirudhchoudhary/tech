# Generated by Django 2.2 on 2019-04-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolcode', models.PositiveIntegerField()),
                ('school_name', models.CharField(max_length=257)),
                ('District', models.CharField(max_length=259)),
                ('Constituencies', models.CharField(max_length=257)),
                ('Mandal', models.CharField(max_length=259)),
                ('lat', models.PositiveIntegerField()),
                ('Long', models.PositiveIntegerField()),
            ],
        ),
    ]
