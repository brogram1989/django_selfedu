from django.db import models
from django.urls import reverse

# Create your models here.

class MwInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name='maqola')
    content = models.TextField(blank=True, verbose_name='maqola matni')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='rasm')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqti')
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name='konfiguratsiya turlari'
        verbose_name_plural='konfiguratsiya turlari'
        ordering = ['time_create','title']



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='ishlab chiqaruvchi nomi')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name='Kotegoriya'
        verbose_name_plural='Kotegoriyalar'
        ordering = ['id']