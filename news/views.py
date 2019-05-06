from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from django.shortcuts import render
# Create your views here.
def welcome(request):
    return render(request,"welcome.html")


def news_of_day(request):
    date=dt.date.today()
    day=convert_dates(date)
    html=f'''
        <html>
            <body>
                <h1>News for {day} {date.day}/{date.month}/{date.year}</h1>
            </body>
        </html>
        '''
    return HttpResponse(html)

def convert_dates(dates):
    day_number=dt.date.weekday(dates)
    days=["Monday","Tuesday","Thursday","Wednesday","Thursday","Friday","Sartuday","Sunday"]
    day=days[day_number]
    return day

def past_days_news(request,past_date):
    try:
        date=dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        raise Http404
    day=convert_dates(date)
    html=f'''
        <html>
            <head><title>Moringa Tribune</title></head>
            <body>
            <h1> News for {day} {date.day}/{date.month}/{date.year}</h1>
            <button style='padding:10px';border='1px solid #587';>Click me</button>
            <canvas style='border=1px solid black';>Do it here</canvas>
            </body>
        </html>
        '''


    return HttpResponse(html)
