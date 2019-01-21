# Generated by Django 2.1.5 on 2019-01-17 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_group_group_image'),
        ('TeamMatches', '0002_remove_match_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='group',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='team_group', to='Users.Group'),
            preserve_default=False,
        ),
    ]
