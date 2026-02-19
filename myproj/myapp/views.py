from django.shortcuts import render, HttpResponse
from .models import my_tb

def add_recored(request):
    new_record= my_tb(attribute_1="Na Add and Record!")
    new_record.save()
    return HttpResponse("Record Added!<br><a href='/show'>Show Records</a>")

def show_record(request):
    all_data = my_tb.objects.all()

    html_output = "<h1>STORED RECORDS:</h1>"
    for item in all_data:
        html_output += f"<li>{item.attribute_1}</li>"
    html_output += f"<a href='/add'>Add Another</a>"    
    return HttpResponse(html_output)


