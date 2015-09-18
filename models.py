from django.db import models

class Header(models.Model):
    image = models.ImageField("Header", upload_to="img/")

class Show(models.Model):
    show_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    time_slot_from = models.IntegerField(default=0)
    time_slot_to = models.IntegerField(default=1)
    audio_files = models.ForeignKey('AudioFiles')
    image = models.ImageField("Show Image", upload_to="img/")
    email = models.CharField(max_length=50)    
    
    def __str__(self):
        return self.show_name

class AudioFiles(models.Model):
    audio_file = models.FileField(upload_to="audio/")
    episode = models.IntegerField(default=1)

    def __str__(self):
        return str(self.audio_file)

class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.title

