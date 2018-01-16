from django.shortcuts import render
 
 
def error_404(request):
        data = {}
        return render(request,'ADEL/templates/404.html', data)
 
def error_500(request):
        data = {}
        return render(request,'ADEL/templates/500.html', data)