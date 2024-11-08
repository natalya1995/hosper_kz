from django.db import models
from pytils.translit import slugify


class Image(models.Model):
    image = models.ImageField("Фото", upload_to="images/")
    stand = models.ForeignKey('Stand', on_delete=models.CASCADE, related_name="images", null=True, blank=True)
    smokehouse = models.ForeignKey('Smokehouse', on_delete=models.CASCADE, related_name="images", null=True, blank=True)
    hosper = models.ForeignKey('Hosper', on_delete=models.CASCADE, related_name="images", null=True, blank=True)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"Image for {self.stand or self.smokehouse or self.hosper}"


class Stand(models.Model):
    model = models.CharField("Модель", max_length=100)
    size = models.CharField("Размер", max_length=50)
    material = models.CharField("Материал", max_length=100)
    weight = models.IntegerField("Вес в кг")
    descriptions = models.TextField("Описание")
    price = models.IntegerField("Цена")
    availability = models.IntegerField("Наличие")
    slug = models.SlugField(unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = "Подставка"
        verbose_name_plural = "Подставки"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.model)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.model


class Smokehouse(models.Model):
    model = models.CharField("Модель", max_length=100)
    size = models.CharField("Размер", max_length=50)
    material = models.CharField("Материал", max_length=100)
    weight = models.IntegerField("Вес в кг")
    lattice = models.CharField("Решётка", max_length=100)
    descriptions = models.TextField("Описание")
    price = models.IntegerField("Цена")
    availability = models.IntegerField("Наличие")
    slug = models.SlugField(unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = "Коптильня"
        verbose_name_plural = "Коптильни"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.model)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.model


class Hosper(models.Model):
    model = models.CharField("Модель", max_length=100)
    size = models.CharField("Размер", max_length=50)
    material = models.CharField("Материал", max_length=100)
    descriptions = models.TextField("Описание")
    weight = models.IntegerField("Вес в кг")
    manufacturer = models.CharField("Производитель", max_length=100)
    lattice = models.CharField("Решётка", max_length=100)
    smokehouse = models.ForeignKey(Smokehouse, on_delete=models.CASCADE, verbose_name="Коптильня", null=True, blank=True)
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE, verbose_name="Подставка", null=True, blank=True)
    price = models.IntegerField("Цена")
    availability = models.IntegerField("Наличие")
    slug = models.SlugField(unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = "Хоспер"
        verbose_name_plural = "Хосперы"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.model)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.model
