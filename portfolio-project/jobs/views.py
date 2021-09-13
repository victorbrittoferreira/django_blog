from django.shortcuts import render

from .models import Job

#def home(request):
    #import pdb; pdb.set_trace()

    ##vry fcking important
    #print('*******')
    #print(jobs)
    #print('*******')
    #print(request)
    #print('*******')
    #print(dir(request))
    #print('*******')
    
    #jobs = Job.objects.all()


def home(request):
    jobs = Job.objects
    
    return render( request, 'jobs/home.html', {'jobs':jobs})


# Create your views here.
