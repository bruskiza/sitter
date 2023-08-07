from io import BytesIO
import base64

import qrcode

from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

from pathlib import Path

# Create your models here.

class Seat(models.Model):
    name = models.CharField(max_length=100)
    what3words_address = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def return_image():
        return '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'
    
    def generate_qr_code(self):
        w3w_url = f'https://map.what3words.com/{self.what3words_address}'
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(w3w_url)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        qr_image.save(buffer, format='PNG')
        buffer.seek(0)

        qr_base64 = base64.b64encode(buffer.read()).decode('utf-8')
        return qr_base64