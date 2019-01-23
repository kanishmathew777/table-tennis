# Generated by Django 2.1.5 on 2019-01-22 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('match_status', models.IntegerField(choices=[(1, 'COMPLETED'), (2, 'LIVE'), (3, 'SCHEDULED')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('team1_score', models.IntegerField(default=0)),
                ('team2_score', models.IntegerField(default=0)),
                ('set_name', models.IntegerField(choices=[(1, 'Set 1'), (2, 'Set 2'), (3, 'Set 3')], default=1)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_name', to='TeamMatches.Match')),
            ],
            options={
                'ordering': ['set_name'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_group', to='Users.Group')),
                ('players', models.ManyToManyField(related_name='player', to='Users.Player')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamone', to='TeamMatches.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamtwo', to='TeamMatches.Team'),
        ),
        migrations.AlterUniqueTogether(
            name='set',
            unique_together={('match', 'set_name')},
        ),
    ]
