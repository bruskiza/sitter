from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User


import qrcode


def w3w_qrcode(words):

    # Generate the What3Words URL
    w3w_url = f'https://map.what3words.com/{words}'

    # Generate the QR code
    qr_code = qrcode.make(w3w_url)

    # Save the QR code as an image
    return qr_code

    
class Building(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Floor(models.Model):
    name = models.CharField(max_length=100)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    

class Seat(models.Model):
    name = models.CharField(max_length=100)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    what_three_word = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.floor.building.name}-{self.floor.name}-{self.name}"


class Allocation(models.Model):
    

    
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def display_image(self):
        qr = w3w_qrcode(self.seat.what_three_word)
        data = 'iVBORw0KGgoAAAANSUhEUgAAApsAAAC4CAYAAACsNSfVAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAZdEVYdFNvZnR3YXJlAEFkb2JlIEltYWdlUmVhZHlxyWU8AACw60lEQVR4Xu2dBWAURxfHH5aQhHhChITg7u7u7u5FSqFF6qVQN'
        return format_html('<img src="data:image/png;base64,{}"/>', data)
    
    display_image.short_description = 'Image'
    
    def __str__(self) -> str:
        return f"{self.seat} - {self.owner.username}"

