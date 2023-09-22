from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productattachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattachment',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]