from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
#Diccionario de datos
monthly_challenges = {
    "january": "Jugar basquetball al menos dos veces a la semana",
    "february" : "Ir al gym 6 veces a la semana",
    "march": "Caminar 20 minutos cada dia de la semana",
    "april": "Jugar basquetball al menos dos veces a la semana",
    "may": "Ir al gym 6 veces a la semana",
    "june": "Caminar 20 minutos cada dia de la semana",
    "july": "Jugar basquetball al menos dos veces a la semana",
    "august" : "Ir al gym 6 veces a la semana",
    "september": "Caminar 20 minutos cada dia de la semana",
    "october" : "Jugar basquetball al menos dos veces a la semana",
    "november": "Ir al gym 6 veces a la semana",
    "december": "Caminar 20 minutos cada dia de la semana"
}

def index(request):
    list_items = ""
    months =list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge",args=[month])
        list_items += f" <li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request,month):
    months= list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge",args=[redirect_month]) #/challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(response,month):
    try:
        challenge_text = monthly_challenges[month]
        response =f"<h1>{challenge_text}</h1>"
        return HttpResponse(response)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")

    