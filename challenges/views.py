from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

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
    "December": "Caminar 20 minutos cada dia de la semana"
}


def monthly_challenge_by_number(request,month):
    return HttpResponse(month)

def monthly_challenge(response,month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported")

    return HttpResponse(challenge_text)