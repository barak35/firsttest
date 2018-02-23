from django.shortcuts import render
import price
import auth

# Create your views here.
from django.http import JsonResponse

def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : [price.korbit.highXRP,  '3', '4', '5']
    })