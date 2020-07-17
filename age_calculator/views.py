from django.http import HttpResponse
from django.shortcuts import render
from datetime import date


def calculator(request):
    return render(request, 'calc.html')


def output(request):
    fname = (request.GET.get('text', 'default'))
    birthdate = (request.GET.get('date', 'default'))
    birthmonth = (request.GET.get('month', 'default'))
    birthyear = (request.GET.get('year', 'default'))

    present_date = date.today().day 
    present_month = date.today().month
    present_year = date.today().year

    if int(birthdate) >= int(present_date) and int(birthmonth) >= int(present_month):

        dd = (int(present_date) + 30) - (int(birthdate))
        mm = (int(present_month-1)+int(12)) - (int(birthmonth))
        yy = (int(present_year) - int(1))-(int(birthyear))

        params = {'fname': fname, 'bdate': dd, 'bmonth': mm, 'byear': yy}
        return render(request, 'result.html', params)

    elif int(birthdate) >= int(present_date) and int(birthmonth) <= int(present_month):

        dd = (int(present_date) + 30) - int(birthdate)
        mm = (int(present_month)-1) - int(birthmonth)
        yy = (int(present_year)-int(birthyear))
        params = {'fname': fname, 'bdate': dd, 'bmonth': mm, 'byear': yy}
        return render(request, 'result.html', params)

    elif int(birthdate) <= int(present_date) and int(birthmonth) > int(present_month):

        dd = (int(present_date) - int(birthdate))
        mm = (int(present_month) + 12) - int(birthmonth)
        yy = (int(present_year) - 1)-int(birthyear)
        params = {'fname': fname, 'bdate': dd, 'bmonth': mm, 'byear': yy}
        return render(request, 'result.html', params)

    elif int(birthdate) <= int(present_date) and int(birthmonth) <= int(present_month):

        dd = (int(present_date)-int(birthdate))
        mm = (int(present_month)-int(birthmonth))
        yy = (int(present_year)-int(birthyear))
        params = {'fname': fname, 'bdate': dd, 'bmonth': mm, 'byear': yy}
        return render(request, 'result.html', params)

    return HttpResponse('error')
