from django.shortcuts import render, get_object_or_404

from .models import Job
def alljobs(request):
    job = Job.objects
    return render(request, 'job/alljobs.html', {'job':job})

def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'job/detail.html', {'job':job})

