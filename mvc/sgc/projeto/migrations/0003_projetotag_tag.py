# Generated by Django 3.2.3 on 2021-06-02 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0002_rename_projetopesquisa_projeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetotag',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='projeto.tag'),
            preserve_default=False,
        ),
    ]