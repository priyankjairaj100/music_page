from django.db import models

class ALbum(models.Model):
    atrist=models.CharField(max_length=100)
    album_title=modles.CharField(max_length=100)
    genre=models.Charfield(max_length=100)
    album_logo=models.ChaField(max_length=1000)
    
class Song(models.Model):
    album=models.ForiegnKey(Albums,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.charField(max_length=100)
    
