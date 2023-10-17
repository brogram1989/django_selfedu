# Generated by Django 4.2.4 on 2023-09-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mw_info', '0002_category_mwinfo_cat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Kotegoriya', 'verbose_name_plural': 'Kotegoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='mwinfo',
            options={'ordering': ['time_create', 'title'], 'verbose_name': 'konfiguratsiya turlari', 'verbose_name_plural': 'konfiguratsiya turlari'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='ishlab chiqaruvchi nomi'),
        ),
        migrations.AlterField(
            model_name='mwinfo',
            name='content',
            field=models.TextField(blank=True, verbose_name='maqola matni'),
        ),
        migrations.AlterField(
            model_name='mwinfo',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='rasm'),
        ),
        migrations.AlterField(
            model_name='mwinfo',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='mwinfo',
            name='title',
            field=models.CharField(max_length=255, verbose_name='maqola'),
        ),
    ]