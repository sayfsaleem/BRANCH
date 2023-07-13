from django.db import models

class Student(models.Model):
    student_id = models.PositiveIntegerField(unique=True, default=10000)
    Name = models.CharField(max_length=60, blank=False, null=False)
    FatherName = models.CharField(max_length=60, blank=False, null=False)
    CourseName = models.CharField(max_length=60, blank=False, null=False)
    AdmissionDate = models.DateField()
    CompletionDate = models.DateField()
    certificate = models.FileField(upload_to='certificates/', blank=True, null=True)
    qrcode = models.ImageField(upload_to='qrcodes/', blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.pk:
            last_student = Student.objects.order_by('-student_id').first()
            if last_student:
                self.student_id = last_student.student_id + 1
        super().save(*args, **kwargs)
class Event(models.Model):
    Title = models.CharField(max_length=60,blank=None, null=False)
    Youtube_Video_Link = models.URLField(blank=None,null=None)
    Date = models.DateField(blank=None,null=None)
    Function = models.CharField(max_length=40,help_text="Function name like Open House, Certfication Day and Picnic etc")
