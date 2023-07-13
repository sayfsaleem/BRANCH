from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
from .models import Student,Event
import os
from django.shortcuts import render
from django.conf import settings
from main.models import Student
# Create your views here.
class HomeView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Event.objects.all()
        context['info'] = data
        return context
    template_name = 'index2.html'
def CertificateView(request, student_id):
    try:
        # Retrieve the student based on the provided ID
        student = Student.objects.get(student_id=student_id)

        # Define the path to the student's certificate image file
        certificate_path = os.path.join(settings.MEDIA_ROOT, 'certificates', f'{student.Name}Certificate.png')

        # Check if the certificate image file exists
        if not os.path.exists(certificate_path):
            return HttpResponse("Certificate not found.")

        # Generate the URL for the certificate image
        certificate_url = os.path.join(settings.MEDIA_URL, 'certificates', f'{student.Name}Certificate.png')

        # Render the about.html template with the certificate URL and student context
        return render(request, 'about.html', {'certificate_url': certificate_url})
    except :
        return HttpResponse("Following Student Data not found")
