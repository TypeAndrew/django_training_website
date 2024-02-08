from django.db import models

# Create your models here.
class PriceCard(models.Model):
    pc_value = models.CharField(max_length=20, verbose_name='Ціна')
    pc_description = models.CharField(max_length=200, verbose_name='Опис')

    def __str__(self):
        return self.pc_value

    class Meta:
        verbose_name = 'Ціна'
        verbose_name_plural = 'Ціни'

class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name='Послуга')
    pt_old_price = models.CharField(max_length=200, verbose_name='Стара цінав')
    pt_price = models.CharField(max_length=200, verbose_name='Нова ціна')

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = 'Послуга'
        verbose_name_plural = 'Послуги'