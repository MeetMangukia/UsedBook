# Generated by Django 2.2.7 on 2019-11-20 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20191120_1240'),
        ('product', '0002_book_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.BookSeller'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='book_category',
            field=models.CharField(max_length=200),
        ),
    ]
