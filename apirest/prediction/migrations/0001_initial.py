# Generated by Django 2.1.5 on 2019-02-10 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_1', models.IntegerField()),
                ('id_2', models.IntegerField()),
                ('cmp_fname_c1', models.FloatField()),
                ('cmp_fname_c2', models.FloatField()),
                ('cmp_lname_c1', models.FloatField()),
                ('cmp_lname_c2', models.FloatField()),
                ('cmp_sex', models.FloatField()),
                ('cmp_bd', models.FloatField()),
                ('cmp_bm', models.FloatField()),
                ('cmp_by', models.FloatField()),
                ('cmp_plz', models.FloatField()),
                ('is_match', models.BooleanField()),
            ],
        ),
    ]
