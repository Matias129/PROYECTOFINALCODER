# Generated by Django 4.1.2 on 2022-12-15 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0003_post_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
