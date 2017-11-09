from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Post
import MySQLdb







def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

"""def good_pay(request):
    return render(request, 'blog/pay.html')"""

def good_pay(request):
    db = MySQLdb.connect(host='VrKing99.mysql.pythonanywhere-services.com',    # your host, usually localhost
                 user='VrKing99',         # your username
                 passwd='werbowe99',  # your password
                 db='VrKing99$telegrambot',
                 charset='utf8')        # name of the data base

    cursor2 = db.cursor()
    sql2="select tel from user_info limit 1;"
    cursor2.execute(sql2)
    data_sms =  cursor2.fetchall()
    if 'q' in request.GET:
        message = 'You searched for: %r %s' % (request.GET['q'],data_sms[0][0])
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
