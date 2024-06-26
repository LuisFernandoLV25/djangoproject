from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound


def monthly_challenge_by_number(request,month):
    return HttpResponse(month)

def monthly_challenges(response,month):
    challenge_text = None
    if month == "january":
        challenge_text = "Jugar basquetball al menos dos veces a la semana"
    elif month == "february":
        challenge_text = "Ir al gym 6 veces a la semana"
    elif month == "march":
        challenge_text = "Caminar 20 minutos cada dia de la semana"
    else:
        return HttpResponseNotFound(challenge_text)
    
    return HttpResponse("Page not found")