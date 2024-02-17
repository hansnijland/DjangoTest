from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Wielrenner 
from .models import Voetbalspeler


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts': posts})
def wielrenner_list(request):
    wielrenners = Wielrenner.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/wielrenner_list.html',{'wielrenners': wielrenners})
def Voetbalspeler_list(request): 
    voetbalspelers = Voetbalspeler.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/Voetbalspeler_list.html',{'voetbalspelers': voetbalspelers})


