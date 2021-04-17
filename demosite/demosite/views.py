from django.http import HttpResponse
def home(request):
        return HttpResponse('<h1>Hello from Django</h1>')
def about(request):
        return HttpResponse('<h1>This is About Page</h1>')
def contact(request):
        return HttpResponse('<h1>9511989870</h1>')
def address(request):
        return HttpResponse('<h1>a/p: savalaj tal:tasgon dist:sangli</h1>')
def technology(request):
        return HttpResponse('<h1>Artificial intelligence</h1>')
def Web(request):
        return HttpResponse('<h1>instagram</h1>')
def mobile(request):
        return HttpResponse('<h1>I.phone</h1>')
def Desktop(request):
        return HttpResponse('<h1>linux</h1>')