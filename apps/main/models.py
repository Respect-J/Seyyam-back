from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title_ru = models.CharField(max_length=256, verbose_name="Слоган на русском", default="test")
    title_uz = models.CharField(max_length=256, verbose_name="Слоган на узбекском", default="test")
    title_en = models.CharField(max_length=256, verbose_name="Слоган на английском", default="test")


    class Meta:
        abstract = True


class Maintitle(BaseModel):


    def __str__(self):
        return "Слоган"

    class Meta:
        verbose_name = "Заголовок сайта"
        verbose_name_plural = "Заголовок сайта"


class Contacts(models.Model):
    first_contact = models.CharField(max_length=256, verbose_name="первый контакт")
    second_contact = models.CharField(max_length=256, verbose_name="второй контакт")

    def __str__(self):
        return "контакты"

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


class Banners(BaseModel):
    img = models.ImageField(upload_to="img/banners/", verbose_name="Фото")
    description_uz = models.TextField(verbose_name="Описание на узбекском", default="test")
    description_en = models.TextField(verbose_name="Описание на английском", default="test")
    description_ru = models.TextField(verbose_name="Описание на русском", default="test")

    def __str__(self):
        return f"карусель: {self.title_ru}"

    class Meta:
        verbose_name = "Карусель"
        verbose_name_plural = "Карусель"


class Projects(BaseModel):
    img = models.ImageField(upload_to="img/banners/", verbose_name="фото")

    def __str__(self):
        return f"проект: {self.title_ru}"

    class Meta:
        verbose_name = "Проекты"
        verbose_name_plural = "Проекты"


class Collections(models.Model):
    numimg = models.CharField(max_length=1, default="1", verbose_name="номер фото")
    img = models.ImageField(upload_to="img/collections/", verbose_name="фото")

    def __str__(self):
        return f"фото под номером {self.numimg}"

    class Meta:
        verbose_name = "Коллекции фото"
        verbose_name_plural = "Коллекции фото"


class Services(BaseModel):
    img = models.ImageField(upload_to="img/Service/", verbose_name="фото")
    description_uz = models.TextField(verbose_name="Описание на узбекском", default="test")
    description_en = models.TextField(verbose_name="Описание на английском", default="test")
    description_ru = models.TextField(verbose_name="Описание на русском", default="test")

    def __str__(self):
        return f"Услуга: {self.title_ru}"

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервис"

