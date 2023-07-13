from django.contrib import admin
from main.models import Student,Event
from django.utils.html import format_html
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('id','student_id')
    search_fields = ('Name','FatherName','CourseName','student_id')
    fields = ('Name','FatherName','CourseName','AdmissionDate','CompletionDate','certificate','qrcode')
    def display_certificate(self, obj):
        if obj.certificate:
            return format_html('<a href="{}" target="_blank">View Certificate</a>', obj.certificate.url)
        return '-'

    display_certificate.short_description = 'Certificate'
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ("Title",)
    fields = ('Title','Function','Youtube_Video_Link','Date')
