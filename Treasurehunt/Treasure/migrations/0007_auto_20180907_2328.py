# Generated by Django 2.1 on 2018-09-07 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Treasure', '0006_treasuregram_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasuregram',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]