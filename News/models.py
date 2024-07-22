from datetime import datetime

from django.db import models

# Create your models here.

class Image(models.Model):
    # اضف حقول الصورة هنا (مثل الصورة نفسها وأي معلومات إضافية)
    image = models.ImageField()
    def __str__(self):
        return self.image.name

class Video(models.Model):
    # اضف حقول الفيديو هنا (مثل الفيديو نفسه وأي معلومات إضافية)
    video = models.FileField()

    def __str__(self):
        return self.video.name




class News(models.Model):
    title_arb = models.CharField(max_length=255)
    title_eng = models.CharField(max_length=255)
    article_arb = models.TextField()
    article_eng = models.TextField()
    main_image = models.ImageField()
    attached_image = models.ManyToManyField(Image, blank=True)  # العلاقة مع الصور
    attached_video = models.ManyToManyField(Video, blank=True)  # العلاقة مع الفيديوات
    date = models.DateField(default=None)

    def __str__(self):
        return self.title_arb

class AboutProsecution(models.Model):
    title_arb = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100)
    article_arb = models.TextField()
    article_eng = models.TextField()
    def __str__(self):
        return self.title_arb

class AttorneyGeneral(models.Model):
    name_arb = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100)
    article_arb = models.TextField()
    article_eng = models.TextField()
    main_image = models.ImageField()
    start_date = models.DateField(default=None, blank=True)



    def __str__(self):
        return self.name_arb
