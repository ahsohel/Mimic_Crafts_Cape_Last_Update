# Generated by Django 3.0.3 on 2022-02-12 06:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicifyapp', '0002_auto_20220212_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table_Special_Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Offer_Name', models.CharField(max_length=255)),
                ('offer_expiry_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Special Offer',
            },
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 12, 12, 44, 42, 342174)),
        ),
        migrations.AlterField(
            model_name='blogs_comments',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 12, 12, 44, 42, 343171)),
        ),
        migrations.AlterField(
            model_name='newsletter_table',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 12, 12, 44, 42, 346185)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 12, 12, 44, 42, 340179)),
        ),
        migrations.AlterField(
            model_name='posted_jobs',
            name='post_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 12, 12, 44, 42, 340179)),
        ),
        migrations.CreateModel(
            name='Table_Special_Offer_Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Percentage', models.IntegerField()),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicifyapp.Categories')),
                ('Offer_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicifyapp.Table_Special_Offer')),
            ],
            options={
                'verbose_name_plural': 'Special Offer Categories',
            },
        ),
    ]
