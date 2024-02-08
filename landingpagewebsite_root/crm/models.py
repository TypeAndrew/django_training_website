from django.db import models

# Create your models here.

class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200,verbose_name="Статус")

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статуси'

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200,verbose_name="Ім'я")
    order_phone = models.CharField(max_length=200,verbose_name="Телефон")
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT,null=True,verbose_name="Статус")

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Безліч замовленнь'

class CommentCrm(models.Model):
    coment_binding = models.ForeignKey(Order,on_delete=models.CASCADE, verbose_name='Заявка')
    coment_text = models.TextField( verbose_name="Текст коментаря")
    coment_dt = models.DateTimeField(auto_now=True, verbose_name="Дата створення")

    def __str__(self):
        return self.coment_text

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'