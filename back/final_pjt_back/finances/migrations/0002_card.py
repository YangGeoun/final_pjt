# Generated by Django 4.2.7 on 2023-11-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finances", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Card",
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
                ("name", models.TextField()),
                ("naver_card_id", models.TextField()),
                ("annual_fee", models.TextField()),
                ("base_performance", models.TextField()),
                ("fuel", models.TextField(blank=True, null=True)),
                ("shoping", models.TextField(blank=True, null=True)),
                ("supermarket", models.TextField(blank=True, null=True)),
                ("convenience_store", models.TextField(blank=True, null=True)),
                ("eat_out", models.TextField(blank=True, null=True)),
                ("cafe_bakery", models.TextField(blank=True, null=True)),
                ("movie", models.TextField(blank=True, null=True)),
                ("public_transport", models.TextField(blank=True, null=True)),
                ("maintenance", models.TextField(blank=True, null=True)),
                ("communication", models.TextField(blank=True, null=True)),
                ("education", models.TextField(blank=True, null=True)),
                ("parenting", models.TextField(blank=True, null=True)),
                ("culture", models.TextField(blank=True, null=True)),
                ("leisure", models.TextField(blank=True, null=True)),
                ("airline_mileage", models.TextField(blank=True, null=True)),
                ("premium", models.TextField(blank=True, null=True)),
                ("hi_pass", models.TextField(blank=True, null=True)),
                ("auto", models.TextField(blank=True, null=True)),
                ("medical", models.TextField(blank=True, null=True)),
                ("beauty", models.TextField(blank=True, null=True)),
                ("points_cashback", models.TextField(blank=True, null=True)),
                ("easy_payment", models.TextField(blank=True, null=True)),
                ("rental", models.TextField(blank=True, null=True)),
                ("pet", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
