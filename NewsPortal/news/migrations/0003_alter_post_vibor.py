# Generated by Django 4.2 on 2023-05-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_entrance_category_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='vibor',
            field=models.CharField(choices=[('AR', 'Статья'), ('NW', 'Новость')], default='AR', max_length=2),
        ),
    ]
