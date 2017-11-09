from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Post





def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

"""def good_pay(request):
    return render(request, 'blog/pay.html')"""

def good_pay(request):

    if 'q' in request.GET:
        message = 'You searched for: %r ' % (request.GET['q'])
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
