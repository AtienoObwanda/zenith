# Generated by Django 3.2.16 on 2022-11-28 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='clasp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Clasps',
            },
        ),
        migrations.CreateModel(
            name='color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='coreMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'coreMaterials',
            },
        ),
        migrations.CreateModel(
            name='mainMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'mainMaterials',
            },
        ),
        migrations.CreateModel(
            name='watchStrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'watchStraps',
            },
        ),
        migrations.CreateModel(
            name='watchType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'watchTypes',
            },
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField(blank=True)),
                ('main_image', models.ImageField(default='images/def.png', upload_to='images/')),
                ('meta_image1', models.ImageField(upload_to='images/')),
                ('meta_image2', models.ImageField(upload_to='images/')),
                ('meta_image3', models.ImageField(upload_to='images/')),
                ('model_image', models.ImageField(upload_to='images/')),
                ('on_sale', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=False)),
                ('in_stock', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch', to='Store.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch', to='Store.category')),
                ('clasp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch', to='Store.clasp')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch', to='Store.color')),
                ('coreMaterial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch', to='Store.corematerial')),
                ('mainMaterial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch', to='Store.mainmaterial')),
                ('watchStrap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch', to='Store.watchstrap')),
                ('watchType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch', to='Store.watchtype')),
            ],
            options={
                'verbose_name_plural': 'watches',
                'ordering': ('-created',),
            },
        ),
    ]
