from django.conf import settings
from django.db import models
from django.urls import reverse


class WatchManager(models.Manager):
    def get_queryset(self):
        return super(WatchManager, self).get_queryset().filter(is_active=True)


class category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse("Store:category_detail", args=[self.slug])

    def __str__(self):
        return self.name


class color(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.name


class brand(models.Model):
    name = models.CharField(max_length=255, db_index= True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta: 
        verbose_name_plural = 'Brands'

    def get_absolute_url(self):
        return reverse("Store:brand_detail", args=[self.slug])

    def __str__(self):
        return self.name


class watchType(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'watchTypes'

    def __str__(self):
        return self.name



class clasp(models.Model):
    name = models.CharField(max_length=255, db_index = True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Clasps'

    def __str__(self):
        return self.name


class watchStrap(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'watchStraps'

    def __str__(self):
        return self.name

class coreMaterial(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'coreMaterials'

    def __str__(self):
        return self.name


class mainMaterial(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'mainMaterials'

    def __str__(self):
        return self.name


# class Reviews(models.Model):
#     pass

class Watch(models.Model):
    title = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank = True)
    main_image = models.ImageField(upload_to='products/', default='images/def.png')
    meta_image1 = models.ImageField(upload_to='products/')
    meta_image2 = models.ImageField(upload_to='products/')
    meta_image3 = models.ImageField(upload_to='products/')
    model_image = models.ImageField(upload_to='products/')
    on_sale = models.BooleanField(default=False)
    is_new = models.BooleanField(default = False)
    in_stock = models.BooleanField(default = True)
    is_active = models.BooleanField(default = True)
    slug = models.SlugField(max_length = 255)
    color = models.ForeignKey(color, related_name='watch', on_delete=models.CASCADE)
    # reviews
    # vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_vendor')
    brand = models.ForeignKey(brand, related_name='watch', on_delete=models.CASCADE)
    category = models.ForeignKey(category, related_name='watch', on_delete=models.CASCADE)
    watchType = models.ForeignKey(watchType, related_name='watch', on_delete=models.CASCADE)
    clasp = models.ForeignKey(clasp, related_name='watch', on_delete=models.CASCADE)
    watchStrap = models.ForeignKey(watchStrap, related_name='watch', on_delete=models.CASCADE)
    coreMaterial = models.ForeignKey(coreMaterial, related_name='watch', on_delete=models.CASCADE)
    mainMaterial = models.ForeignKey(mainMaterial, related_name='watch', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    watch = WatchManager()

    class Meta:
        verbose_name_plural = 'watches'
        ordering = ('-created', )

    def get_absolute_url(self):
        return reverse("Store:watch_detail", args=[self.slug])
    

    def __str__(self):
        return self.title






