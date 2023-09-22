from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productattachment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_price_id',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stripe_product_id',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]