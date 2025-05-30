# Generated by Django 5.2.1 on 2025-05-14 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_group_alter_comment_id_alter_post_id_post_group_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="slug",
            field=models.SlugField(default="default-slug", unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="group",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="group",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]
