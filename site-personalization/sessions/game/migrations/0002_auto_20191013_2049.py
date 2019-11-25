# Generated by Django 2.1.1 on 2019-10-13 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='guessed_number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='members',
            field=models.ManyToManyField(through='game.PlayerGameInfo', to='game.Player'),
        ),
        migrations.AddField(
            model_name='player',
            name='owner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='playergameinfo',
            name='game',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='game.Game'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playergameinfo',
            name='player',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playergameinfo',
            name='try_count',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
