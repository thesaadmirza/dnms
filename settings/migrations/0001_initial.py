# Generated by Django 3.0.5 on 2020-04-19 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountGroup',
            fields=[
                ('account_group', models.CharField(max_length=512, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyGroup',
            fields=[
                ('company_group_name', models.CharField(max_length=512, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CountryGroup',
            fields=[
                ('country_group_name', models.CharField(max_length=512, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('currency', models.CharField(max_length=512, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ItemGroup1',
            fields=[
                ('item_group1_name', models.CharField(max_length=512, primary_key=True, serialize=False)),
                ('item_group1_code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LanguageGroup',
            fields=[
                ('language_group_name', models.CharField(max_length=512, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceGroup',
            fields=[
                ('place_group', models.CharField(max_length=512, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('korean', models.CharField(max_length=512, primary_key=True, serialize=False)),
                ('vietnamese', models.TextField(blank=True, null=True)),
                ('english', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnitGroup',
            fields=[
                ('unit_group_name', models.CharField(max_length=512, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ItemGroup2',
            fields=[
                ('item_group2_name', models.CharField(max_length=512, primary_key=True, serialize=False)),
                ('item_group2_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.ItemGroup1')),
            ],
        ),
    ]
