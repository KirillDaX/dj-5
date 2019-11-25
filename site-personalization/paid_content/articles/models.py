from django.contrib.auth.models import AbstractUser
from django.db import models


class Article(models.Model):
    article_title = models.CharField(max_length=150, verbose_name='Название')
    article_image = models.ImageField(verbose_name='Изображение', blank=True)
    article_text = models.TextField(verbose_name='Текст')
    article_free = models.BooleanField(default=False)

    def __str__(self):
        return self.article_title


class User(AbstractUser):
    paid_content = models.BooleanField(default=False)


# логин админа работает, не работает логин обычных пользователей. возможно проблема в АбстрактЮзере
# не понятно почему не работает логин созданных Users
# разделение доступов реализовано через темплейт article ифами
# доделать страницу оплаты
