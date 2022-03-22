# Generated by Django 4.0.3 on 2022-03-22 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyWallz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='wallpapers/')),
                ('category', models.CharField(choices=[('Avengers', 'Avengers'), ('DC', 'DC'), ('Nature', 'Nature'), ('Heros', 'Heros'), ('Motivational', 'Motivational'), ('Sports', 'Sports'), ('Animals', 'Animals'), ('Fantasy', 'Fantasy'), ('Fiction', 'Fiction'), ('History', 'History'), ('Movies', 'Movies'), ('Music', 'Music'), ('Politics', 'Politics')], max_length=200)),
                ('for_what', models.CharField(choices=[('Mobile', 'Mobile'), ('Desktop', 'Desktop'), ('Tablet', 'Tablet')], max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
