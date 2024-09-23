from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Maintitle(BaseModel):
    title = models.CharField(max_length=256, verbose_name="Слоган")

    def __str__(self):
        return "Слоган"

    class Meta:
        verbose_name = "Заголовок сайта"
        verbose_name_plural = "Заголовок сайта"


class Contacts(BaseModel):
    first_contact = models.CharField(max_length=256, verbose_name="первый контакт")
    second_contact = models.CharField(max_length=256, verbose_name="второй контакт")

    def __str__(self):
        return "контакты"

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


class Banners(BaseModel):
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    img = models.ImageField(upload_to="img/banners/", verbose_name="Фото")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"карусель: {self.title}"

    class Meta:
        verbose_name = "Карусель"
        verbose_name_plural = "Карусель"


class Projects(BaseModel):
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    img = models.ImageField(upload_to="img/banners/", verbose_name="фото")

    def __str__(self):
        return f"проект: {self.title}"

    class Meta:
        verbose_name = "Проекты"
        verbose_name_plural = "Проекты"


class Collections(BaseModel):
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    img = models.ImageField(upload_to="img/collections/", verbose_name="фото")

    def __str__(self):
        return "наши коллекции"

    class Meta:
        verbose_name = "Коллекции фото"
        verbose_name_plural = "Коллекции фото"


class Services(BaseModel):
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    img = models.ImageField(upload_to="img/Service/", verbose_name="фото")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"Услуга: {self.title}"

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервис"

