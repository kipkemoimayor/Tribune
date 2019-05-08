from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from django.shortcuts import render,redirect
# Create your views here.
# def welcome(request):
#     return render(request,"welcome.html")


def news_of_day(request):
    date=dt.date.today()
    return render(request,"all-news/today-news.html",{"date":date})
#
# def convert_dates(dates):
#     day_number=dt.date.weekday(dates)
#     days=["Monday","Tuesday","Thursday","Wednesday","Thursday","Friday","Sartuday","Sunday"]
#     day=days[day_number]
#     return day

def past_days_news(request,past_date):
    try:
        date=dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        raise Http404
        assert False
    if date==dt.date.today():
        return redirect(news_of_day)
    # day=convert_dates(date)


    return render(request,"all-news/past-news.html",{"date":date})
