from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from django.shortcuts import render,redirect
from .models import Article
# Create your views here.
# def welcome(request):
#     return render(request,"welcome.html")


def news_of_day(request):
    date=dt.date.today()
    news=Article.today_news()
    return render(request,"all-news/today-news.html",{"date":date,'news':news})
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
    news=Article.days_news(date)

    return render(request,"all-news/past-news.html",{"date":date,'news':news})

def search_results(request):
    if 'article' in request.GET and request.GET['article']:
        search_term=request.GET.get('article')
        search_articles=Article.search_by_title(search_term)
        message=f'{search_term}'

        return render(request,'all-news/search.html',{'message':message,'articles':search_articles})

    else:
        message="You haven't  searched for any term"
        return render(request,'all-news/search.html',{'message':message})
