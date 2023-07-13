import os
import qrcode
from PIL import Image, ImageDraw, ImageFont
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.core.files import File
from .models import Student

@receiver(post_save, sender=Student)
def create_certificate(sender, instance, created, **kwargs):
    if created:
        # Paths
        base_dir = settings.MEDIA_ROOT
        cert_template_path = os.path.join(base_dir, 'certificates', 'cert.png')
        output_cert_path = os.path.join(base_dir, 'certificates', f"{instance.Name}certificate.png")
        qr_path = os.path.join(base_dir, 'qrcodes', f"{instance.Name}_qrcode.png")
        font_path = os.path.join(base_dir, 'arial.ttf')

        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(f"http://127.0.0.1/certificate/{instance.student_id}")
        qr.make(fit=True)

        qr_img = qr.make_image(fill='black', back_color='white')
        qr_img.save(qr_path)

        # Open the main image
        image = Image.open(cert_template_path)

        # Paste the QR code
        qr_image_modified = Image.open(qr_path).resize((230,230))
        image.paste(qr_image_modified, (1330,210))

        # Initialize the drawing context
        draw = ImageDraw.Draw(image)

        # Define the text content and style
        texts = [instance.Name, instance.FatherName, instance.CourseName,
                 instance.AdmissionDate.strftime('%Y-%m-%d'),
                 instance.CompletionDate.strftime('%Y-%m-%d'),
                 str(instance.student_id)]

        font_size = 30

        # Load the font
        font = ImageFont.truetype(font_path, font_size)

        # Define positions
        positions = [(815, 456), (1200, 456), (1050, 500), (1050, 620), (1050, 660), (1390, 415)]

        # Draw all the text on the image with black color
        for pos, t in zip(positions, texts):
            draw.text(pos, t, font=font, fill=(0, 0, 0))  # Black color (RGB value)

        # Save the modified image
        image.save(output_cert_path)

        # Save the qr code and certificate path to the Student instance
        instance.certificate.save(f"{instance.Name}certificate.png", File(open(output_cert_path, 'rb')), save=True)
        instance.qrcode.save(f"{instance.Name}_qrcode.png", File(open(qr_path, 'rb')), save=True)
