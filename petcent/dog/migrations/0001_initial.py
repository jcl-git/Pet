# Generated by Django 4.2.16 on 2024-11-21 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to="dog/images/", verbose_name="狗狗照片"),
                ),
                ("title", models.CharField(max_length=100, verbose_name="狗狗品种")),
                (
                    "price",
                    models.CharField(max_length=100, null=True, verbose_name="狗狗价格"),
                ),
                ("description", models.CharField(max_length=250, verbose_name="狗狗简介")),
                ("url", models.URLField(blank=True, verbose_name="狗狗资源")),
            ],
            options={
                "verbose_name": "狗狗",
                "verbose_name_plural": "狗狗",
            },
        ),
    ]
