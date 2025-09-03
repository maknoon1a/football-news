from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406419612',
        'name': 'Ahmad Omar Mohammed Maknoon',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)